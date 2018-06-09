import sys
import requests
from pprint import pprint
import hello_helper


url = 'https://ws-api.iextrading.com/1.0'
batch = '/stock/aapl/chart'

#comment
r = requests.get(url+batch, auth=('user', 'pass')) 
r.status_code
r.headers['content-type']

data = r.json()
a = hello_helper.class1(r[0]['high'], 

print(data[0]['low'])
