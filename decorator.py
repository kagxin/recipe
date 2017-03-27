#!/usr/bin/python3

import logging
import time
import functools

logging.basicConfig(level=logging.DEBUG)

"""用类去写装饰器更加的灵活
"""
#被装饰的函数，作为类对象初始化参数，然后调用的__call__方法
class use_logging_class(object):
    """docstring for use_logging_class"""
    def __init__(self, func):
        super(use_logging_class, self).__init__()  
        self._func = func             

    def __call__(self, *args, **kwargs):        
        start = time.time()
        self._func(*args, **kwargs)
        usetime = time.time()-start
        print("{0} func use time {1}.".format(self._func.__name__, usetime))



def use_logging(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        usetime = time.time()-start
        print("{0} func use time {1}.".format(func.__name__, usetime))
        
    return wrapper


#在装饰器的外面再封装一层变成，带参数的装饰器
def use_logging_with_arg(p = True):
    def use_logging(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            func(*args, **kwargs)
            usetime = time.time()-start
            if p:
                print("{0} func use time {1}.".format(func.__name__, usetime))
        return wrapper
    return use_logging

@use_logging_with_arg(False)
def foo():
    print('i am foo func.')
    # logging.info('foo is running')
@use_logging_class
def bar():
    print('i am bar func.')



foo()
print(foo.__name__)


bar()