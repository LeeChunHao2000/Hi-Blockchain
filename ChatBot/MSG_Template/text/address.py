import requests

from linebot.models import *

def text_get_search_ethereum_address(address):
    if len(address) != 42:
        return TextSendMessage(
            text = f'| Hi BlockChain |\n\n'
            f'地址長度必須為 42'
            )

    try:
        data  = requests.get(f'https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey=JBCZPAPNUIRFTFFG5JSCUD5DEW9UT3QYYT').json()['result']
        price = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=twd,usd').json()['ethereum']
        usdt  = requests.get(f'https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress=0xdac17f958d2ee523a2206206994597c13d831ec7&address={address}&tag=latest&apikey=JBCZPAPNUIRFTFFG5JSCUD5DEW9UT3QYYT').json()['result']
    except Exception as e:
        print ('Error! problem is {}'.format(e.args[0]))
    data = data.zfill(19)
    usdt = usdt.zfill(7)
    balance = data[:-18] + '.' + data[-18:-14]
    ethusd = format(float(balance) * price['usd'], '.2f')
    ethtwd = format(float(balance) * price['twd'], '.2f')
    Ubalance = usdt[:-6] + '.' + usdt[-6:-2]

    return TextSendMessage(
            text = f'| Hi BlockChain |\n\n'
            f'|錢包地址| {address}\n\n'
            f'|乙太餘額| {balance} ETH\n'
            f'|美金估值| {ethusd} USD\n'
            f'|台幣估值| {ethtwd} TWD\n\n'
            f'|泰達餘額| {Ubalance} USDT'
            )
    
def text_get_search_bitcoin_address(address):
    if len(address) != 34:
        return TextSendMessage(
            text = f'| Hi BlockChain |\n\n'
            f'地址長度必須為 34'
            )

    try:
        data = requests.get(f'https://chain.api.btc.com/v3/address/{address}', headers={'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}).json()
        price = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=twd,usd').json()
    except Exception as e:
        print ('Error! problem is {}'.format(e.args[0]))

    usd, twd = price['bitcoin']['usd'], price['bitcoin']['twd']
    receive  = format(float(data['data']['received'] / 100000000), '.4f')
    send     = format(float(data['data']['sent'] / 100000000), '.4f')
    balance  = format(float(data['data']['balance'] / 100000000), '.4f')
    btcusd = format(float(balance) * usd, '.2f')
    btctwd = format(float(balance) * twd, '.2f')

    return TextSendMessage(
            text = f'| Hi BlockChain |\n\n' +
            f'|錢包地址| {address}\n\n' +
            f'|比特餘額| {balance} BTC\n' +
            f'|累計接收| {receive} BTC\n' +
            f'|累計發送| {send} BTC\n' +
            f'|美金估值| {btcusd} USD\n' +
            f'|台幣估值| {btctwd} TWD'
            )

# text_get_search_bitcoin_address('1CVyyJ6C8z3t5g25BJ8sBSqpwXTdz3HKiy')