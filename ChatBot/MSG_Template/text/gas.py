import requests

from linebot.models import *

# Gas
def text_gas():
    try:
        data = requests.get('https://ethgasstation.info/api/ethgasAPI.json').json()
    except Exception as e:
        print ('Error! problem is {}'.format(e.args[0]))
    safeLow, average, fast= data['safeLow']/10, data['average']/10, data['fast']/10
    return TextSendMessage(
            text = f'| Hi BlockChain |\n\n'
            f'慢速 (<30m) => {safeLow}\n'
            f'中等 (<5m) => {average}\n'
            f'快速 (<2m) => {fast}\n\n'
            f'單位: Gwei (Gas Price)，乙太坊當前手續費 (礦工費)\n\n')