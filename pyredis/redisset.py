#coding:utf8
import redis

r = redis.Redis('192.168.1.2')
r.sadd('myset', 'mysql', 'redis', 'pgsql')
r.sadd('myset2', 'mysql', 'redis', 'pgsql', 'cacash')
print(r.scard('myset'))
#差集
print(r.sdiff('myset2', 'myset'))
r.sdiffstore('myset2-myset', 'myset2', 'myset')

print(r.smembers('myset2-myset'))

#交集
print(r.sinter('myset', 'myset2'))
r.sinterstore('myset&myset2', 'myset', 'myset2')

#并集
r.sunionstore('myset|myset2', 'myset', 'myset2')
print(r.smembers('myset|myset2'))


print(r.sismember('myset', 'redis'))
r.smove('myset2', 'myset', 'cacash')
print(r.spop('myset|myset2'))
print(r.srandmember('myset&myset2', 2))
print(r.srem('myset', 'redis'))