# bitkubchecker.py

import requests
from pprint import pprint
import time

API_HOST = 'https://api.bitkub.com'
mycoin = ['THB_BTC',
          'THB_ETH',
          'THB_DOGE',
          'THB_ETH',
          'THB_LTC',
          'THB_USDT',
          'THB_XRP',
          'THB_KSM']


def CheckPrice():
    response = requests.get(API_HOST + '/api/market/ticker')
    result = response.json()

    #pprint(result['THB_BTC'])

    alltext = ''
    
    for c in mycoin:
        #sym = 'THB_BTC'
        sym = c
        data = result[sym]
        last = data['last']
        #print(data)
        print(sym, last)
        pchange = data['percentChange']
        text = '{} price: {:,.3f} ({})'.format(sym,last,pchange)
        alltext += text + '\n' # alltext = alltext + text
        
    #print(type(last))
    v_result.set(alltext)
    print('-----')
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




























