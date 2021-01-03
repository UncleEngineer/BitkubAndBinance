#algocheck.py

condition = {'THB_BTC':{'buy':950000,'sell':1080000},
             'THB_ETH':{'buy':20000,'sell':30000},
             'THB_DOGE':{'buy':0.389,'sell':0.4}}


#print(condition['THB_BTC'])

def CheckCondition(coin,price):
    # coin= 'THB_BTC', price = 1050000
    text = ''
    check_buy = condition[coin]['buy']
    if price <= check_buy:
        txt = '{} ราคาลงแล้ว เหลือ: {:,.3f} รีบซื้อด่วน!\n(ราคาที่อยากได้: {:,.3f})'.format(coin,price,check_buy)
        print(txt)
        text += txt + '\n'

    check_sell = condition[coin]['sell']
    if price >= check_sell:
        txt = '{} ราคาขึ้นแล้ว ล่าสุดเป็น: {:,.3f} รีบขายด่วน!\n(ราคาที่อยากขาย: {:,.3f})'.format(coin,price,check_sell)
        print(txt)
        text += txt + '\n'

    return text


CheckCondition('THB_ETH',60000)




