import requests

from linebot.models import *

# Gas
def text_gas():
    try:
        data = requests.get('https://ethgasstation.info/api/ethgasAPI.json').json()
    except Exception as e:
        print ('Error! problem is {}'.format(e.args[0]))
    return TextSendMessage(
            text = f'| Grenade Bot |\n\n'
            f'慢速 (<30m) => {data['safeLow']/10}\n'
            f'中等 (<5m) => {data['average']/10}\n'
            f'快速 (<2m) => {data['fast']/10}\n\n'
            f'單位: Gwei (Gas Price)，乙太坊當前手續費 (礦工費)\n\n')