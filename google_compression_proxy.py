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
    return 's=CjMKEwjJ3f_w3d7fAhXNKZYKHcj8CzsSDAj-5NjhBRDsmaGDARoJCgdkZWZhdWx0OICk9AMSSDBGAiEApuVLMIRFc9N_bMzO4lf9xQveFXtPbVU3dBJ4iWntidsCIQDuCpa2KjcRb6Y6Da34Lw4UOdYoHoV12Oh0ciyo7ANJVA==, c=win, b=3578, p=98'

def get(url, headers={}, **kwargs):

    proxies = {
        'http': 'http://compress.googlezip.net:80',
        'https': 'https://proxy.googlezip.net:443',
    }

    proxy_headers = {
        'Chrome-Proxy': get_google_header(),
        # 'chrome-proxy-ect': '4G',
    }

    proxy = proxies['http']

    if url.startswith('http://'):
        url = url[7:]
        proxy = proxies['http']
    elif url.startswith('https://'):
        url = url[8:]
        proxy = proxies['https']

    path_idx = url.find('/')
    if path_idx == -1:
        host = url
        path = '/'
    else:
        host = url[:path_idx]
        path = url[path_idx:]

    proxy_headers.update({'Host': host})

    if 'headers' in kwargs.keys():
        proxy_headers.update(kwargs.pop('headers'))

    return requests.get('{proxy}{path}'.format(proxy=proxy, path=path),
                        headers=proxy_headers, **kwargs)