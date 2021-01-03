# bitkubchecker.py

import requests
from pprint import pprint
import time
from songline import Sendline
# pip install songline
token = 'bgClpKkgX4c4o0k0pAMLmd7pfSgSotcGpHAF0tT8N43'
messenger = Sendline(token)

line_condition = True

API_HOST = 'https://api.bitkub.com'
mycoin = ['THB_BTC',
          'THB_ETH',
          'THB_DOGE',
          'THB_ETH',
          'THB_LTC',
          'THB_USDT',
          'THB_XRP',
          'THB_KSM']


condition = {'THB_BTC':{'buy':950000,'sell':1005000},
             'THB_ETH':{'buy':20000,'sell':30000},
             'THB_DOGE':{'buy':0.389,'sell':0.4}}


#print(condition['THB_BTC'])

def CheckCondition(coin,price):
    # coin= 'THB_BTC', price = 1050000
    text = ''
    check_buy = condition[coin]['buy']
    if price <= check_buy:
        txt = '{} ราคาลงแล้ว เหลือ: {:,.3f} รีบซื้อด่วน!\n(ราคาที่อยากได้: {:,.3f})'.format(coin,price,check_buy)
        #print(txt)
        text += txt + '\n'

    check_sell = condition[coin]['sell']
    if price >= check_sell:
        txt = '{} ราคาขึ้นแล้ว ล่าสุดเป็น: {:,.3f} รีบขายด่วน!\n(ราคาที่อยากขาย: {:,.3f})'.format(coin,price,check_sell)
        #print(txt)
        text += txt + '\n'

    return text



current_text = ''


def CheckPrice():
    global current_text
    response = requests.get(API_HOST + '/api/market/ticker')
    result = response.json()

    #pprint(result['THB_BTC'])

    alltext = ''
    text_line = ''
    
    for c in mycoin:
        #sym = 'THB_BTC'
        sym = c
        data = result[sym]
        last = data['last']
        #print(data)
        #print(sym, last)
        pchange = data['percentChange']
        text = '{} price: {:,.3f} ({})'.format(sym,last,pchange)
        alltext += text + '\n' # alltext = alltext + text
        if line_condition == True:
            if c in condition:
                checktext = CheckCondition(c,last)
                if len(checktext) > 0:
                    text_line += checktext
                    
    # เงื่อนไขที่จะส่งไลน์ (ดูคลิปเลย)               
    if line_condition == True and current_text != text_line:
        print('Condition: ',text_line)
        current_text = text_line
        # sendline
        messenger.sendtext(text_line)
        
        
        
        
        
    #print(type(last))
    v_result.set(alltext)
    #print('-----')
    R1.after(100,CheckPrice)
    # .after คือ การทำให้ R1 มีการ refresh ทุก 200 ms เรียกฟังชั่น CheckPrice
    


######################GUI######################

from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.geometry('500x600')
GUI.title('โปรแกรมเช็คราคาจาก Bitkub')

FONT1 = ('Angsana New',30)

L1 = ttk.Label(GUI,text='ราคา bitkub ล่าสุด',font=FONT1)
L1.pack()

#B1 = ttk.Button(GUI,text='Check!',command=CheckPrice)
#B1.pack(ipadx=20,ipady=10)

v_result = StringVar()
v_result.set('--------result--------')
R1 = ttk.Label(textvariable=v_result,font=FONT1)
R1.pack()

#Run ฟังชั่นทุกครั้งที่เปิด
CheckPrice()
GUI.mainloop()




























