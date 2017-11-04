import bisect

valid_characters = '`abcdefghijklmnopqrstuvwxyz{'     

def find_prefix_range(prefix):
    # 在字符列表中查找前缀字符所处的位置。
    posn = bisect.bisect_left(valid_characters, prefix[-1:]) 
    # 找到前驱字符。
    suffix = valid_characters[(posn or 1) - 1]  
    # 返回范围。
    return prefix[:-1] + suffix + '{', prefix + '{' 

print(find_prefix_range('abc'))

import time


def foo():
    return ''.join(('a', 'b', 'c'))


print(time.time())
now = time.time()
foo()
print(time.time()-now)