#coding:utf-8
'''
Created on 2017��6��7��

@author: ilinkin
'''

import stackless

channel = stackless.channel()

def receiving_tasklet():
    print "Recieving tasklet started"
    print channel.receive()
    print "Receiving tasklet finished"

def sending_tasklet():
    print "Sending tasklet started"
    channel.send("send from sending_tasklet")
    print "sending tasklet finished"
    
def another_tasklet():
    print "Just another tasklet in the scheduler"
    
    
stackless.tasklet(receiving_tasklet)()
stackless.tasklet(sending_tasklet)()
stackless.tasklet(another_tasklet)()
stackless.run()

"""
接收的微进程调用 channel.receive() 的时候，便阻塞住，这意味着该微进程暂停执行，直到有信息从这个通道送过来。除了往这个通道发送信息以外，没有其他任何方式可以让这个微进程恢复运行。

若有其他微进程向这个通道发送了信息，则不管当前的调度到了哪里，这个接收的微进程都立即恢复执行；而发送信息的微进程则被转移到调度列表的末尾，就像调用了 stackless.schedule() 一样。

同样注意，发送信息的时候，若当时没有微进程正在这个通道上接收，也会使当前微进程阻塞:
"""
print("{}".format("************************************"))

stackless.tasklet(sending_tasklet)()
stackless.tasklet(another_tasklet)()
stackless.run()
stackless.tasklet(another_tasklet)()
stackless.run()
stackless.tasklet(receiving_tasklet)()
stackless.run()
"""
发送信息的微进程，只有在成功地将数据发送到了另一个微进程之后，才会重新被插入到调度器中。
"""

