#coding:utf-8

'''
Created on 2017��6��7��

@author: ilinkin
'''
import stackless
import time

def print_x(x):
    print("1", x)
    stackless.schedule()
    print("2", x)
    stackless.schedule()
    print("3", x)
    stackless.schedule()    



stackless.tasklet(print_x)('one')
stackless.tasklet(print_x)('two')
stackless.tasklet(print_x)('three')

stackless.run()


print('program end!')

"""
当调用 stackless.schedule() 的时候，当前活动微进程将暂停执行，
并将自身重新插入到调度器队列的末尾，
好让下一个微进程被执行。
一旦在它前面的所有其他微进程都运行过了，
它将从上次 停止的地方继续开始运行。这个过程会持续，
直到所有的活动微进程都完成了运行过程。
这就是使用stackless达到合作式多任务的方式。
"""