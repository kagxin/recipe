#coding:utf-8
import redis

r = redis.Redis('192.168.1.2')
r.hset('myhash', 'field1', 'foo1')
r.hset('myhash', 'field2', 'foo2')
print(r.hget('myhash', 'field2'))
print(r.hexists('myhash', 'field1'))
print(r.hgetall('myhash'))
r.hincrby('myhash', 'field3', 3)
# r.hincrbyfloat('myhash', 'field3', 3.3)
print(r.hkeys('myhash'))
print(r.hlen('myhash'))
print(r.hmget('myhash', 'field1', 'field2', 'field3'))
#redis 基础不支持hash嵌套，当python redis客户端帮我们实现了这一部分。
r.hmset('myhash2', {'field1':{'infield1':'12'}})
print(r.hget('myhash2', 'field1'))
print(r.hvals('myhash'))
print(r.hscan('myhash2'))
