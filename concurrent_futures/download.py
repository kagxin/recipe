from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
import requests
from requests.exceptions import ConnectionError
from functools import partial
from os import cpu_count


def get_url(url):
    try:
        r = requests.get(url)
    except ConnectionError:
        raise ConnectionError('检查网络链接！')

    return url, r.status_code

URLS = [
    'https://my.oschina.net/u/2255341/blog',
    'https://github.com/timeline.json',
    'http://www.oschina.net/',
]


if __name__ == '__main__':
    # get_url('https://github.com/timeline.json')
    executor = ThreadPoolExecutor(max_workers=2)
    for res in executor.map(get_url, URLS):
        print(res)

    print('------------------------------------------------')
    for future in as_completed(map(partial(executor.submit, get_url), URLS)):
        res = future.result()
        print(res)



"""

"""