#coding:utf-8
'''
Created on 2017��6��8��

@author: ilinkin
'''
import time
import stackless
from inspect import stack


channel = stackless.channel()

def revice():
    while True:
        msg = channel.receive()   
        print(msg)
        stackless.schedule()
        
    
def send():
    while True:
        channel.send("form send!")    
        time.sleep(2)

stackless.tasklet(revice)()
stackless.tasklet(send)()

stackless.run()

"""
当协程被recevice阻塞的时候，stackless调度器会自动调到到其他协程，
当recevice从对应的管道接收的数据的时候，立即回复当前的流程。
而发送信息的协程则被转移到调度列表的末尾.
"""


