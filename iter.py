#!/usr/bin/python3

class Fib(object):
    """docstring for Fib"""
    def __init__(self):
        super(Fib, self).__init__()
        self.a = 0
        self.b = 1

    def __next__(self):     #一个实现__next__方法的对象是一个迭代器，一个实现__iter__方法的对象是可迭代的，
                            #python2中next是一个函数，python3中next是一个特殊方法__next__

        self.a, self.b = self.a+self.b, self.a
        return self.a

    def __iter__(self):
        return self

fibs = Fib()

for i in fibs:
    if i>1000:
        print(i)
        break


