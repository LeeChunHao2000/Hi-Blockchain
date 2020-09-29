import requests

from linebot.models import *

def text_usdt():
    try:
        max  = format(float(requests.get('https://max-api.maicoin.com/api/v2/trades?market=usdttwd&page=1&limit=1').json()[0]['price']), '.2f')
        bito = format(float(requests.get('https://api.bitopro.com/v3/trades/usdt_twd').json()['data'][0]['price']), '.2f')
        ace  = format(float(requests.get('https://www.ace.io/polarisex/quote/getKline?baseCurrencyId=1&tradeCurrencyId=14&type=24&limit=1').json()['attachment'][0]['current']), '.2f')
    except Exception as e:
        print ('Error! problem is {}'.format(e.args[0]))

    return TextSendMessage(
            text = f'| Hi BlockChain |\n\n'
            f'|MAX| {max} TWD\n'
            f'|BITO| {bito} TWD\n'
            f'|ACE| {ace} TWD'
            )