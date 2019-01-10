# Not working, on fix (2019/01/10)

# Chrome data saver python

[Chrome data saver](https://chrome.google.com/webstore/detail/data-saver/pfmgfdlgomnbgkofeojodiodmgpgmkac) python interface.

## Usage

```python
import requests
from google_compression_proxy import get as compress_get

response_original = request.get(url)
repr(response_original) # '<Response [200]>'

response_compressed = compress_get(url)
repr(response_compressed) # '<Response [200]>'
```

## Sample

```python
import requests
from google_compression_proxy import get as compress_get

http_image_url = 'http://ichef.bbci.co.uk/wwfeatures/wm/live/624_351/images/live/p0/4v/jy/p04vjy8l.jpg'
https_image_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Siberian_Tiger_by_Malene_Th.jpg/450px-Siberian_Tiger_by_Malene_Th.jpg'

r1 = requests.get(http_image_url)
r2 = compress_get(http_image_url)

print('Original image size:', len(r1.content))
print('Compressed image size:', len(r2.content))
# Original image size: 63816
# Compressed image size: 33361

r1 = requests.get(https_image_url)
r2 = compress_get(https_image_url)

print('Original image size:', len(r1.content))
print('Compressed image size:', len(r2.content))
# Original image size: 93198
# Compressed image size: 93198
```

## Requirements

- requests
