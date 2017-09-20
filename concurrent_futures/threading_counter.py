# coding=gbk
import threading, time
from threading import RLock, Lock, Condition, Event

count = 0

def print_hello(*args, **kwargs):
    print(args, kwargs)


class TimerCircle(threading.Timer):
    def run(self):
        while True:
            self.finished.wait(self.interval)
            # if not self.finished.is_set():
            self.function(*self.args, **self.kwargs)
            # self.finished.set()

t = TimerCircle(1, print_hello, 'hello')
t.start()

# t = threading.Timer(1, print_hello, 'hello')
# t.start()


class Counter(threading.Thread):

    def __init__(self, lock, threadName):
        super(Counter, self).__init__(name=threadName)
        self.lock = lock

    def run(self):
        global count
        self.lock.acquire()
        for _ in range(10000):
            count = count + 1
        self.lock.release()


lock = threading.Lock()
for i in range(5):
    Counter(lock, "thread-" + str(i)).start()

print(count)
time.sleep(10)

lock1 = threading.Lock()
def conter(*args):
    print(args)
    global count, lock1
    lock1.acquire()
    for _ in range(10000):
        count = count + 1
    lock1.release()
for i in range(5):
    t = threading.Thread(target=conter, name="thread-"+str(i), args=(1, 2))
    t.start()

"""
threading : 中的4把锁

t = threading.Lock()
t.acquire(blocking=True, timeout=-1)  获取锁，t被释放前一直阻塞
t.release()                           释放t


t = threading.RLock()
t.acquire(blocking=True, timeout=-1)    获取锁在当前线程已经持有锁，则不阻塞，否则阻塞。
t.release()                             释放锁
在同一个线程中，acquire和release个数相同，如果acquire多余release，则当前线程一旦获取锁，其他线程无法获取锁，




threading.Event

t = threading.Condition()
t.acquire(*args)    获取底层锁
t.release()         释放底层锁
t.wait(timeout=None)  
等待通知或直到发生超时。如果调用线程在调用此方法时尚未获取锁，则会引发RuntimeError。该方法释放底层锁，然后阻塞，直到它被另一个线程中的相
同条件变量的notify（）或notify_all（）调用唤醒，或者直到可选的超时发生。一旦唤醒或超时，它会重新获取锁定并返回。
t.wait_for()
t.notify(n=1)
默认情况下，唤醒一个线程等待这个条件（如果有的话）。 如果调用线程在调用此方法时尚未获取锁，则会引发RuntimeError。
该方法最多唤醒等待条件变量的线程n个; 如果没有线程正在等待，它是无效的。
如果至少有n个线程正在等待，则当前的实现将正好唤醒n个线程。 但是，依靠这种行为是不安全的。 未来，优化的实现可能偶尔会唤醒超过n个线程。
注意：一个唤醒的线程实际上不会从其wait（）调用返回，直到它可以重新获取锁定。 由于notify（）不释放锁，其调用者应该。

t.notify_all()
"""


