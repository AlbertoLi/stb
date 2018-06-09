import requests
from pprint import pprint

r = requests.get('https://ws-api.iextrading.com/1.0/tops', auth=('user', 'pass'))
r.status_code
r.headers['content-type']

pprint(r.json())
