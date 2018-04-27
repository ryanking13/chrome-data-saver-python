import requests
from google_compression_proxy import get as compress_get

http_image_url = 'http://ichef.bbci.co.uk/wwfeatures/wm/live/624_351/images/live/p0/4v/jy/p04vjy8l.jpg'
https_image_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Siberian_Tiger_by_Malene_Th.jpg/450px-Siberian_Tiger_by_Malene_Th.jpg'

r1 = requests.get(http_image_url)
r2 = compress_get(http_image_url)

print('Original image size:', len(r1.content))
print('Compressed image size:', len(r2.content))

r1 = requests.get(https_image_url)
r2 = compress_get(https_image_url)

print('Original image size:', len(r1.content))
print('Compressed image size:', len(r2.content))