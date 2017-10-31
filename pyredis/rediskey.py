#coding:utf8

import redis

conn = redis.Redis('192.168.1.2')
conn.set('key_key', 1)
conn.incr('key_key')
conn.incr('key_key', 15)
conn.decr('key_key', 5)
print(conn.get('key_key'))
conn.delete('key_key')
print(conn.get('key_key'))
print(conn.exists('key_key'))
conn.set('key_key', 1)
#添加过期时间
conn.expire('key_key', 60)
print(conn.exists('key_key'))
print(conn.keys('*2'))
#返回key的过期时间 s pttl
print(conn.ttl('key_key'))
# 移除key的过期时间
print(conn.persist('key_key'))

# 从当前数据库中随机返回一个key
print(conn.randomkey())

conn.rename('key_key', 'key_key2')
print(conn.keys())
print(type(conn.type('key_key2')))