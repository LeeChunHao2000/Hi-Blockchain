import requests
import pandas as pd

from talib import abstract
from linebot.models import *

# Config
url = 'https://api.binance.com/'
do_list = {'DEMA': abstract.DEMA, 'SMA': abstract.SMA, 'MA': abstract.MA, 'RSI': abstract.RSI, 'AD': abstract.AD, 'OBV': abstract.OBV}

def get_kline(url, symbol, interval):
    try:
        data = requests.get(url + 'api/v3/klines', params={'symbol': symbol, 'interval': interval}).json()
    except Exception as e:
        print ('Error! problem is {}'.format(e.args[0]))
    tmp  = []
    pair = []
    for base in data:
        tmp  = []
        for i in range(1,6):
            tmp.append(base[i])
        pair.append(tmp)
    df = pd.DataFrame(pair, columns=['open', 'high', 'low', 'close', 'volume'])
    df = df.astype(float)
    return df

def text_index(pair, do, time, period):
    todo = do_list[do]
    kline = get_kline(url, pair, time.lower())
    index = round(todo(kline, int(period)).iloc[-1], 6)
    return TextSendMessage(
            text = f'| Hi BlockChain |\n\n'
            f'|查詢交易對| {pair}\n\n'
            f'|查詢指標| {do}\n'
            f'|K線時框| {time}\n'
            f'|指標時長| {period}\n'
            f'|指標數據| {index}'
            )