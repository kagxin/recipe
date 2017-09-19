from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
# from concurrent.futures import
import requests
from functools import partial

def get_url(url):
    r = requests.get(url)
    print(r.status_code)
    # print(r.content)
    return url, r.status_code

URLS = [
    'https://my.oschina.net/u/2255341/blog',
    'https://github.com/timeline.json',
    'http://www.oschina.net/',
]


if __name__ == '__main__':
    # get_url('https://github.com/timeline.json')
    executor = ThreadPoolExecutor(max_workers=2)

    for future in  as_completed(map(partial(executor.submit, get_url), URLS)):
        res =  future.result()
        print(res)
