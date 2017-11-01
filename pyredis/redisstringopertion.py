#coding:utf8

import redis

conn = redis.Redis('192.168.1.2')

conn.set('s_key', 'hello')
conn.append('s_key', 'world')
print(conn.getrange('s_key', 1, -1))
print(conn.getbit('s_key', 2))
print(conn.getset('s_key', 'hello_world'))
print(conn.mget('s_key', 'key_key2'))
print(conn.setrange('s_key', 6, 'Redis'))
print(conn.get('s_key'))
print(conn.strlen('s_key'))
dct = {'s_key':'helloworld', 'key_key2':'hello_world.'}
print(conn.mset(**dct))