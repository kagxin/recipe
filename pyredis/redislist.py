#coding:utf-8
import redis

conn = redis.Redis('192.168.1.2')
#lpush index[0]
conn.lpush('list_key', 'hello', 'redis', 'redis2')
print(conn.rpush('list_key', '0', '2'))
print(conn.lrange('list_key', 0, 1))
print(conn.blpop('list_key', 12))
print(conn.brpop('list_key', 1))
print(conn.brpoplpush('list_key', 'list_key2', 2))
print(conn.lindex('list_key', 1))
 
# 在遇到的第一个hello之后插入0
print(conn.linsert('list_key', 'after', 'hello', '0'))
print(conn.llen('list_key'))
 
#弹出第一个元素
print(conn.lpop('list_key'))
# count > 0 : 从表头开始向表尾搜索，移除与 VALUE 相等的元素，数量为 COUNT 。
# count < 0 : 从表尾开始向表头搜索，移除与 VALUE 相等的元素，数量为 COUNT 的绝对值。
# count = 0 : 移除表中所有与 VALUE 相等的值。

print(conn.lrem('list_key', 'redis', 2))
print(conn.lset('list_key', 1, 'first'))
print(conn.ltrim('list_key', 0, 2))
print(conn.lrange('list_key', 0, -1))
print(conn.rpop('list_key'))