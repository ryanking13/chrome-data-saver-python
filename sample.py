import requests
from google_proxy import get as proxy_get

blocked_url = 'http://a.blocked.site'

r = requests.get(blocked_url)
print(r.status_code)
# 403

r = proxy_get(blocked_url)
print(r.status_code)
# 200