import hashlib
import hmac
import json
import requests
from pprint import pprint
import pwd
# สร้างไฟล์ pwd.py ขึ้นมา KEY='ddadsfasdfas' , SECRET = b'yasjdkfjaskdf'

# API info
API_HOST = 'https://api.bitkub.com'
API_KEY = pwd.KEY
API_SECRET = pwd.SECRET

def json_encode(data):
	return json.dumps(data, separators=(',', ':'), sort_keys=True)

def sign(data):
	j = json_encode(data)
	#print('Signing payload: ' + j)
	h = hmac.new(API_SECRET, msg=j.encode(), digestmod=hashlib.sha256)
	return h.hexdigest()

# check server time
response = requests.get(API_HOST + '/api/servertime')
ts = int(response.text)
#print('Server time: ' + response.text)

# check balances
header = {
	'Accept': 'application/json',
	'Content-Type': 'application/json',
	'X-BTK-APIKEY': API_KEY,
}
data = {
	'ts': ts,
}
signature = sign(data)
data['sig'] = signature

#print('Payload with signature: ' + json_encode(data))
response = requests.post(API_HOST + '/api/market/balances', headers=header, data=json_encode(data))

#print('Balances: ' + response.text)

data = response.json()
data = data['result']
#print(data)
#sym = 'BTC'
sym = ['BTC','DOGE','THB']

for s in sym:
    price = data[s]['available']
    print('{} คงเหลือ: {}'.format(s,price))










