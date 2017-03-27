#!/usr/bin/python
import time

def reverse(data):                      #生成器函数
    for index in range(len(data)-1, -1, -1):
        yield data[index]

gene = reverse(range(10))

for data in gene:         #
    print(data)
#gene.__next__()

for i in (x*x for x in range(10)):   #生成器表达式
    print(i)



print('----------------------------------------')


def people():
    """类似协程的例子
    """
    print('i am a people.')

    while True:
        try:
            foo = yield                #程序会阻塞在yield这里。foo会接受到来之send的变量
            if foo == 'name':
                print('i am tom')
            elif foo == 'age':
                print('i am 22')
            else:
                print('what do you want!')
        except ValueError:                  #捕获通过throw抛给yield的异常。
            print('i am tired, need sleep!')
            time.sleep(5)
            print('sleep end!')
        except GeneratorExit:              #捕获调用close时的GeneratorExit异常，同时raise StopIteration，这个raise是必须的,否则不会终止
            print('i am dead.')
            raise StopIteration

p = people()
p.__next__()
p.send('name')
p.send('age')
p.send('haha')

p.throw(ValueError)

p.close()

print('the end!')

time.sleep(10)


