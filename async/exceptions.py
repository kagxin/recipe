import asyncio
import logging
from functools import wraps
import functools

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s')

def ignore(errors, default=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except errors:
                return default
        return wrapper
    return decorator


async def handle_exception(task):
    try:
        await task
    except Exception as e:
        logging.exception(str(e))
        print("exception consumed")


def log_asyncio_exception(coro):
    async def handle_exception(*args, **kwargs):
        try:
            return await coro(*args, **kwargs)
        except Exception as e:
            logging.exception(str(e))
            raise
    return handle_exception

async def test():
    while True:
        await asyncio.sleep(1)
        print('hello')


async def bug():
    raise Exception('test except')

@log_asyncio_exception
async def bug2():
    raise Exception('test 2 except')

def test_dec():
    raise Exception('test except')

loop = asyncio.get_event_loop()
loop.set_debug(True)

tasks = [
        asyncio.ensure_future(handle_exception(bug())),
        asyncio.ensure_future(handle_exception(test())),
        asyncio.ensure_future(bug2())
    ]

try:
    loop.run_until_complete(asyncio.wait(tasks))
except Exception:
    print("exception consumed")

"""
三种方式去消费一个协程中的异常：
    1、使用run_until_complete: 这个有局限只能在协程是一个的时候使用，
    2、在业务协程外包裹一个协程来消费这个异常 例如 例子中的： handle_exception
    3、写一个装饰器

"""
