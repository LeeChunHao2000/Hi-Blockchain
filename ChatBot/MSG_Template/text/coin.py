import requests

from linebot.models import *

def no_data(x):
    return 0 if x is None else x

def get_coin_id(symbol):
    try:
        data = requests.get('https://api.coingecko.com/api/v3/coins/list').json()
    except Exception as e:
        print ('Error! problem is {}, symbol is {}'.format(e.args[0], symbol))

    ids = []
    for coin in data:
        if coin['symbol'] == symbol:
            ids.append(coin['id'])

    return ids

def get_market_info(id):
    try:
        data = requests.get(f'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={id}&order=market_cap_desc&sparkline=false&price_change_percentage=1h').json()[0]
    except Exception as e:
        print ('Error! problem is {}, ids is {}'.format(e.args[0], id))

    # None Deal
    for d in data.items():
        data[d[0]] = no_data(d[1])

    name, symbol, volatility, price, rank, ath, athch = data['name'], data['symbol'], round(data['price_change_percentage_24h'], 2), round(data['current_price'], 4), data['market_cap_rank'], round(data['ath'], 4), round(data['ath_change_percentage'], 2)

    text = f'| {name} ({symbol.upper()}) {volatility}% |\n\n' + \
           f'| 當前價格 | {price} USD\n' + \
           f'| 市值排名 | {rank}\n' + \
           f'| 歷史高點 | {ath} USD\n' + \
           f'| 高點回落 | {athch}%'
    
    return text

def text_get_search_coin_market_info(symbol):
    ids = get_coin_id(symbol)
    text = '| Hi BlockChain |'
    for id in ids:
        text += '\n\n' + get_market_info(id)

    return TextSendMessage(text=text)