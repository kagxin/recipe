
一、什么时future？
        1、标准库中这样说，The Future class encapsulates the asynchronous execution of a callable. 

        流畅的python这样说，期物封装待完成的操作，可以放入队列，完成的状态可查询，得到结果（或抛出异常）后可以获取结果（或异常）。
        安道将future翻译为期物还是很形象的，安道翻译的书质量还是有保证的。

        2、从原码看Future的对象有5种状态，封装了一把锁，一个状态值，结果，异常，和回调函数。
        状态分别通过cancelled，running，done，来查询。
        通过set_result，和set_exception来设置结果和异常，并触发回调函数，回调函数只有一个参数就是future本身，在回调函数中可以获取该future绑定操作的结果。
        通过result获取最终结果，如果有异常就raise该异常。可以通过exception获取异常，并没有raise该异常。
        concurrent.futures.ThreadPoolExecutor设置结果、异常的线程和获取结果的线程不再一个线程，这个时候self._condition这一把锁就起了作用，
        而且这把锁也是在future绑定的操作未完成之前，通过result()方法获取结果时阻塞的原因。
        3、concurrent.futures中，与其说future是封装了一个操作，不如说是每一个future绑定了一个操作。


_STATE_TO_DESCRIPTION_MAP = {
    PENDING: "pending",
    RUNNING: "running",
    CANCELLED: "cancelled",
    CANCELLED_AND_NOTIFIED: "cancelled",
    FINISHED: "finished"
}
class Future(object):
    def __init__(self):
        self._condition = threading.Condition()
        self._state = PENDING
        self._result = None
        self._exception = None
        self._waiters = []
        self._done_callbacks = []

    def _invoke_callbacks(self):
        for callback in self._done_callbacks:
            try:
                callback(self)
            except Exception:
                LOGGER.exception('exception calling callback for %r', self)
    def cancel(self):
        with self._condition:
            if self._state in [RUNNING, FINISHED]:
                return False

            if self._state in [CANCELLED, CANCELLED_AND_NOTIFIED]:
                return True

            self._state = CANCELLED
            self._condition.notify_all()

        self._invoke_callbacks()
        return True

    def cancelled(self):
        with self._condition:
            return self._state in [CANCELLED, CANCELLED_AND_NOTIFIED]

    def running(self):
        with self._condition:
            return self._state == RUNNING

    def done(self):
        with self._condition:
            return self._state in [CANCELLED, CANCELLED_AND_NOTIFIED, FINISHED]

    def __get_result(self):
        if self._exception:
            raise self._exception
        else:
            return self._result

    def add_done_callback(self, fn):
        with self._condition:
            if self._state not in [CANCELLED, CANCELLED_AND_NOTIFIED, FINISHED]:
                self._done_callbacks.append(fn)
                return
        fn(self)

    def result(self, timeout=None):
        with self._condition:
            if self._state in [CANCELLED, CANCELLED_AND_NOTIFIED]:
                raise CancelledError()
            elif self._state == FINISHED:
                return self.__get_result()

            self._condition.wait(timeout)

            if self._state in [CANCELLED, CANCELLED_AND_NOTIFIED]:
                raise CancelledError()
            elif self._state == FINISHED:
                return self.__get_result()
            else:
                raise TimeoutError()

    def exception(self, timeout=None):
        with self._condition:
            if self._state in [CANCELLED, CANCELLED_AND_NOTIFIED]:
                raise CancelledError()
            elif self._state == FINISHED:
                return self._exception

            self._condition.wait(timeout)

            if self._state in [CANCELLED, CANCELLED_AND_NOTIFIED]:
                raise CancelledError()
            elif self._state == FINISHED:
                return self._exception
            else:
                raise TimeoutError()


    def set_running_or_notify_cancel(self):
        with self._condition:
            if self._state == CANCELLED:
                self._state = CANCELLED_AND_NOTIFIED
                for waiter in self._waiters:
                    waiter.add_cancelled(self)
                # self._condition.notify_all() is not necessary because
                # self.cancel() triggers a notification.
                return False
            elif self._state == PENDING:
                self._state = RUNNING
                return True
            else:
                LOGGER.critical('Future %s in unexpected state: %s',
                                id(self),
                                self._state)
                raise RuntimeError('Future in unexpected state')

    def set_result(self, result):
        with self._condition:
            self._result = result
            self._state = FINISHED
            for waiter in self._waiters:
                waiter.add_result(self)
            self._condition.notify_all()
        self._invoke_callbacks()

    def set_exception(self, exception):
        with self._condition:
            self._exception = exception
            self._state = FINISHED
            for waiter in self._waiters:
                waiter.add_exception(self)
            self._condition.notify_all()
        self._invoke_callbacks()

        注意：当在线程池内部发生异常的时候并不会直接raise该异常而是通过futures的set_exception()方法将异常暂时封装到future中。当future封装的操作完成的时候，通过其result()方法获取结果是会raise在线程池内部发生的exception。
    二、ThreadPoolExecutor，在什么地方创建的线程，如何控制的线程个数。
        1、ThreadPoolExecutor有一个任务队列，一个保存线程对象的set
        2、在init方法中可以看出，线程池默认最大线程个数为（ cpu个数*5 ）
            if max_workers is None:
                max_workers = (os.cpu_count() or 1) * 5
        3、在submit方法中将一个future对象，和一个操作绑定到一个_WorkItem任务中，
            在其run方法中会把fn操作的结果和异常放到对应的future中，没有一个fn对应一个future，
            submit返回这个future。所以可以在线程池外通过futrue对于fn的状态进行查询，并获取fn的结果或其异常。
            之后将_WorkItem的对象丢到任务队列中。
        4、在submit中判断线程数，如果线程数未达到最大线程数，就新建线程。
            新建的线程target为_worker，_worker的任务就是取出任务queue中的_WorkItem然后run。

class _WorkItem(object):
    def __init__(self, future, fn, args, kwargs):
        self.future = future
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    def run(self):
        if not self.future.set_running_or_notify_cancel():
            return

        try:
            result = self.fn(*self.args, **self.kwargs)
        except BaseException as e:
            self.future.set_exception(e)
        else:
            self.future.set_result(result)
def _worker(executor_reference, work_queue):
    try:
        while True:
            work_item = work_queue.get(block=True)
            if work_item is not None:
                work_item.run()
                # Delete references to object. See issue16284
                del work_item
                continue
            executor = executor_reference()
            # Exit if:
            #   - The interpreter is shutting down OR
            #   - The executor that owns the worker has been collected OR
            #   - The executor that owns the worker has been shutdown.
            if _shutdown or executor is None or executor._shutdown:
                # Notice other workers
                work_queue.put(None)
                return
            del executor
    except BaseException:
        _base.LOGGER.critical('Exception in worker', exc_info=True)
class ThreadPoolExecutor(_base.Executor):
    def submit(self, fn, *args, **kwargs):
        with self._shutdown_lock:
            if self._shutdown:
                raise RuntimeError('cannot schedule new futures after shutdown')

            f = _base.Future()
            w = _WorkItem(f, fn, args, kwargs)

            self._work_queue.put(w)
            self._adjust_thread_count()
            return f
    submit.__doc__ = _base.Executor.submit.__doc__

    def _adjust_thread_count(self):
        # When the executor gets lost, the weakref callback will wake up
        # the worker threads.
        def weakref_cb(_, q=self._work_queue):
            q.put(None)
        # TODO(bquinlan): Should avoid creating new threads if there are more
        # idle threads than items in the work queue.
        if len(self._threads) < self._max_workers:
            t = threading.Thread(target=_worker,
                                 args=(weakref.ref(self, weakref_cb),
                                       self._work_queue))
            t.daemon = True
            t.start()
            self._threads.add(t)
            _threads_queues[t] = self._work_queue


 三、为什么Executor.map按可迭代的顺序返回参数，而as_completed会先返回完成的future?

        1、Executor实现了map方法，ThreadPoolExecutor集成了它。
        2、Executor的map方法先调用submit方法，将对应操作fn，丢到线程池中，并获得一个future List，
            然后通过迭代这个列表依次获取对应future中的结果。
        3、as_completed是先查询所有fs（future）的状态，然后返回已经完成的future，客户端代码会先获取的已经完成的future，
           然后不断检查获取已完成的future，然后返回，所以与提交任务的顺序无关会先返回完成的任务。
def as_completed(fs, timeout=None):
    if timeout is not None:
        end_time = timeout + time.time()

    fs = set(fs)
    with _AcquireFutures(fs):
        finished = set(
                f for f in fs
                if f._state in [CANCELLED_AND_NOTIFIED, FINISHED])
        pending = fs - finished
        waiter = _create_and_install_waiters(fs, _AS_COMPLETED)

    try:
        yield from finished

        while pending:
            if timeout is None:
                wait_timeout = None
            else:
                wait_timeout = end_time - time.time()
                if wait_timeout < 0:
                    raise TimeoutError(
                            '%d (of %d) futures unfinished' % (
                            len(pending), len(fs)))

            waiter.event.wait(wait_timeout)

            with waiter.lock:
                finished = waiter.finished_futures
                waiter.finished_futures = []
                waiter.event.clear()

            for future in finished:
                yield future
                pending.remove(future)

    finally:
        for f in fs:
            with f._condition:
                f._waiters.remove(waiter)

class Executor(object):
    def map(self, fn, *iterables, timeout=None, chunksize=1):

        if timeout is not None:
            end_time = timeout + time.time()

        fs = [self.submit(fn, *args) for args in zip(*iterables)]

        # Yield must be hidden in closure so that the futures are submitted
        # before the first iterator value is required.
        def result_iterator():
            try:
                for future in fs:
                    if timeout is None:
                        yield future.result()
                    else:
                        yield future.result(end_time - time.time())
            finally:
                for future in fs:
                    future.cancel()
        return result_iterator()

四、futures 未完成时为什么会在Executor.map，和as_completed方法阻塞？
    1、self._condition.wait(timeout)这把锁是阻塞的原因，
        调用result的客户端代码，和调用set_result、set_exception的线程池代码不在一个线程中，
        只有在future对应的任务完成之后，线程池中的线程通过set_result、set_exception中的            
        self._condition.notify_all()，重新唤醒wait的客户端代码线程。
        这个时候阻塞解除，获取到对应的已完成的future。

class Future(object):
    def result(self, timeout=None):
        with self._condition:
            if self._state in [CANCELLED, CANCELLED_AND_NOTIFIED]:
                raise CancelledError()
            elif self._state == FINISHED:
                return self.__get_result()

            self._condition.wait(timeout)

            if self._state in [CANCELLED, CANCELLED_AND_NOTIFIED]:
                raise CancelledError()
            elif self._state == FINISHED:
                return self.__get_result()
            else:
                raise TimeoutError()
