# binancechecker.py
from binance.client import Client
import time

api_key = '8k5aWsymxIZDl4Uy8Hx7yOGTk0saNr6rfOi28a1IpCALoipyqUPDLG6sh1K7TbbI'
api_secret = 'f3nx3WodmmoifDQeI7I2vVMEptN9HYoCYhUnLl1X2iLpuMFyHM9saugAePOhFuN8'
client = Client(api_key, api_secret)

#depth = client.get_order_book(symbol='BTCBUSD')
#print(depth)


mycoin = ['BTCBUSD','DOGEBUSD','ETHBUSD']
mycoin = ['BTCBUSD']

while True:
    prices = client.get_all_tickers() #request ใหม่ทุกครั้ง
    for p in prices:
        for c in mycoin:
            sym = c
            if p['symbol'] == sym:
                #print(p)
                pc = float(p['price']) #ราคาบิทคอยหน่อย usd
                rate = 30.01
                cal = pc * rate
                print('เหรียญ: {} ราคา: {:,.8f} บาท'.format(sym,cal))
                print('ราคา USD: {}'.format(pc))
                print('------')
    time.sleep(0.2)
        
