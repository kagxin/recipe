# coding=gbk
import threading, time

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



threading.RLock
threading.Event
threading.Condition

"""
threading.Lock.ac

