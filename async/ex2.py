import sys


msg = 'sadfasdfad'
write, flush = sys.stdout.write, sys.stdin.flush

write(msg)
flush()
write('\x08')

sys.stdout.flush()


print('---------------')


status = '|' + ' ' + msg
write(status)
flush()
write('\x08' * (len(status)-5))


