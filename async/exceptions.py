import asyncio
import logging
from functools import wraps
import functools
import uuid
from textwrap import dedent

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s')


async def handle_exception(task):
    try:
        await task
    except Exception as e:
        logging.exception(str(e))
        print("exception consumed")

async def test():
    while True:
        await asyncio.sleep(1)
        print('hello')


async def bug():
    raise Exception('test except')


def test_dec():
    raise Exception('test except')

loop = asyncio.get_event_loop()
loop.set_debug(True)

tasks = [
        asyncio.ensure_future(handle_exception(bug())),
        asyncio.ensure_future(handle_exception(test()))
    ]

try:
    loop.run_until_complete(asyncio.wait(tasks))
except Exception:
    print("exception consumed")

"""
两种方式去消费一个协程中的异常：
    1、使用run_until_complete: 这个有局限只能在协程是一个的时候使用，
    2、在业务协程外包裹一个协程来消费这个异常 例如 例子中的： handle_exception

"""
