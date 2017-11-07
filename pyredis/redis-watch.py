import redis
from redis import WatchError
import pickle

r = redis.Redis()


def set_cache(name, value, expire=None):
    with r.pipeline() as pipe:
        while True:
            try:
                pipe.watch(name)
                pipe.multi()
                pipe.set(name, pickle.dumps(value))
                if expire:
                    pipe.expire(name, expire)
                pipe.execute()
                break
            except WatchError:
                continue


def get_cache(name):
    with r.pipeline() as pipe:
        while True:
            try:
                pipe.watch(name)
                pipe.multi()
                pipe.get(name)
                res = pipe.execute()
                if res and res[0]!=None:
                    return pickle.loads(res[0])
                else:
                    return None
            except WatchError:
                continue

def delete_cache(name):
    return r.delete(name)

if __name__ == '__main__':
    set_cache('hello', 'world')
    print(get_cache('hello'))
    print(get_cache('not-have'))
    print(delete_cache('hello'))
    print(get_cache('hello'))

