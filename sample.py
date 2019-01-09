import requests
from google_compression_proxy import get as compress_get

http_image_url = 'http://check.googlezip.net/probe/image.jpg'
https_image_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Siberian_Tiger_by_Malene_Th.jpg/450px-Siberian_Tiger_by_Malene_Th.jpg'

print('Testing HTTP')
r1 = requests.get(http_image_url)
r2 = compress_get(http_image_url)

print('Original image size:', len(r1.content))
print('Compressed image size:', len(r2.content))

print('Testing HTTPS')
r1 = requests.get(https_image_url)
r2 = compress_get(https_image_url)
print('Original image size:', len(r1.content))
print('Compressed image size:', len(r2.content))