import requests

from linebot.models import *

def text_btcvix():
    try:
        data = requests.get(f'https://api.alternative.me/fng/').json()
    except Exception as e:
        print ('Error! problem is {}'.format(e.args[0]))
    name, value, sitiuation = data['name'], data['data'][0]['value'], data['data'][0]['value_classification']
    return TextSendMessage(
            text = f'| Hi BlockChain |\n\n'
            f'|指數名稱| {name}\n'
            f'|指數數值| {value}\n'
            f'|當前狀態| {sitiuation}')