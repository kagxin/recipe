#coding:utf8
import redis
import operator
r = redis.Redis('192.168.1.2')
r.zadd('zset_key', 'zset', 10, 'jack', 2000, 'tom', 3000, 'ming', 5000)
r.zadd('zset_key2', 'zset', 10, 'jack', 2000, 'tom', 3000, 'ming', 5000, 'xiao', 6000)

print(r.zcard('zset_key'))
print(r.zcount('zset_key', 1000, 4000))
r.zincrby('zset_key', 'zset', 1)

# 交集  聚合函数可以为 min max sum
r.zinterstore('zset_key&zset_key2', ['zset_key', 'zset_key2'], aggregate='min')
print(r.zscan('zset_key&zset_key2', 0))
#并集
r.zunionstore('zset_key&zset_key2', ['zset_key', 'zset_key2'], aggregate='min')
r.zscan('zset_key&zset_key2', 0)

print(r.zrange('zset_key', 0, 1, withscores=True))
print(r.zrem('zset_key', 'jack'))

print(r.zrangebyscore('zset_key', 0, 10000, withscores=True))
print(r.zrank('zset_key', 'ming'))
print(r.zscore('zset_key2', 'jack'))

