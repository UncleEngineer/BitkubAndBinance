apikey = 'afadaasafsdfasdfafadaasafsdfasdf' 
apisecret = b'afadaasafsdfasdfafadaasafsdfasdf'

#API KEY , API SECRET นำมาจากลิ้งค์นี้ https://www.bitkub.com/publicapi
# ห้ามลบตัว b ออกหน้ารหัส ของ apisecret

import hashlib
import hmac
import json
import requests


# API info
API_HOST = 'https://api.bitkub.com'
API_KEY = apikey
API_SECRET = apisecret

def json_encode(data):
	return json.dumps(data, separators=(',', ':'), sort_keys=True)

def sign(data):
	j = json_encode(data)
	print('Signing payload: ' + j)
	h = hmac.new(API_SECRET, msg=j.encode(), digestmod=hashlib.sha256)
	return h.hexdigest()

# check server time
response = requests.get(API_HOST + '/api/servertime')
ts = int(response.text)
print('Server time: ' + response.text)

# place ask
header = {
	'Accept': 'application/json',
	'Content-Type': 'application/json',
	'X-BTK-APIKEY': API_KEY,
}
data = {
	'sym': 'THB_DOGE',
	'amt': 100, # amount you want to sell
	'rat': 0.27,
	'typ': 'limit',
	'ts': ts,
}
signature = sign(data)
data['sig'] = signature

print('Payload with signature: ' + json_encode(data))
response = requests.post(API_HOST + '/api/market/place-ask', headers=header, data=json_encode(data))


print('Response: ' + response.text)