from hashlib import md5
import random
import time
import requests


# code from https://github.com/cnbeining/Chrome-Data-Compression-Proxy-Standalone-Python/blob/master/google.py
def get_long_int():
    """None->int
    get a looooooong integer."""
    return str(random.randint(100000000, 999999999))


# code from https://github.com/cnbeining/Chrome-Data-Compression-Proxy-Standalone-Python/blob/master/google.py
def get_google_header():
    """None->str
    As in https://github.com/cnbeining/datacompressionproxy/blob/master/background.js#L10-L18 .
    P.S: This repo is a fork of the original one on google code.
    """
    authValue = 'ac4500dd3b7579186c1b0620614fdb1f7d61f944'
    timestamp = str(int(time.time()))
    return 'ps=' + timestamp + '-' + get_long_int() + '-' + get_long_int() + '-' + get_long_int() + ', sid=' + md5((timestamp + authValue + timestamp).encode('utf-8')).hexdigest() + ', b=2403, p=61, c=win'


def get(url, headers={}, **kwargs):

    proxy_headers = {
        'Chrome-Proxy': get_google_header(),
    }

    if url.startswith('http://'):
        url = url[7:]
    elif url.startswith('https://'):
        url = url[8:]
    proxy_headers.update({'Host': url})

    if 'headers' in kwargs.keys():
        proxy_headers.update(kwargs.pop('headers'))

    return requests.get('http://compress.googlezip.net:80', headers=proxy_headers, **kwargs)