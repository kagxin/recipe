import gevent
from gevent.event import Event, AsyncResult

evt = Event()

def setter():
    print('A: Hey wait for me, I have to do something')
    gevent.sleep(3)
    print("Ok, I'm done")
    evt.set()

def waiter():
    print("I'll wait for you!")
    evt.wait()
    print("It's about time")

def main():
    gevent.joinall([
        gevent.spawn(setter),
        gevent.spawn(waiter),
        gevent.spawn(waiter),
        gevent.spawn(waiter),
        gevent.spawn(waiter),
        gevent.spawn(waiter),
])

a = AsyncResult()

def setter1():
    gevent.sleep(3)
    a.set("hello funture")

def waiter1():
    print(a.get())

def main1():
    gevent.joinall([
        gevent.spawn(setter1),
        gevent.spawn(waiter1)
])

if __name__ == '__main__':
    main1()