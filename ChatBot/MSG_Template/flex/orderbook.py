import requests

from linebot.models import *

def get_orderbook(pair):
    try:
        data = requests.get(f'https://max-api.maicoin.com/api/v2/depth?market={pair}&limit=1&sort_by_price=true').json()
        current = requests.get(f'https://max-api.maicoin.com/api/v2/tickers/{pair}').json()['last']
    except Exception as e:
        print ('Error! promblem is {}'.format(e.args[0]))
    return [data['asks'][0][0], data['bids'][0][0], current]
    
def flex_usdt_orderbook():
    btc = get_orderbook('btcusdt')
    eth = get_orderbook('ethusdt')
    bch = get_orderbook('bchusdt')
    timestamp = requests.get('https://max-api.maicoin.com/api/v2/timestamp').json()

    flex_message = FlexSendMessage(
        alt_text = "MAX 美金訂單簿",
        contents = {
                    "type": "carousel",
                    "contents": [
                        {
                        "type": "bubble",
                        "size": "giga",
                        "header": {
                            "type": "box",
                            "layout": "horizontal",
                            "backgroundColor": "#00bce4",
                            "contents": [
                            {
                                "type": "image",
                                "url": "https://www.bangchak.co.th/img/logo.png",
                                "aspectRatio": "137:40",
                                "size": "md",
                                "align": "start"
                            },
                            {
                                "type": "text",
                                "weight": "bold",
                                "size": "md",
                                "gravity": "center",
                                "align": "end",
                                "color": "#FFFFFF",
                                "text": "Max 美金訂單簿"
                            }
                            ]
                        },
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "margin": "md",
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "filler"
                                },
                                {
                                    "type": "text",
                                    "text": "買一",
                                    "color": "#111111",
                                    "weight": "bold",
                                    "size": "sm",
                                    "align": "end"
                                },
                                {
                                    "type": "text",
                                    "text": "賣一",
                                    "color": "#111111",
                                    "weight": "bold",
                                    "size": "sm",
                                    "align": "end"
                                },
                                {
                                    "type": "text",
                                    "text": "最新",
                                    "size": "sm",
                                    "color": "#111111",
                                    "weight": "bold",
                                    "align": "end"
                                }
                                ]
                            },
                            {
                                "type": "separator",
                                "color": "#cccccc",
                                "margin": "md"
                            },
                            {
                                "margin": "md",
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "image",
                                    "url": "https://assets.coingecko.com/coins/images/1/small/bitcoin.png?1547033579",
                                    "aspectRatio": "120:48"
                                },
                                {
                                    "type": "text",
                                    "text": btc[0],
                                    "color": "#111111",
                                    "weight": "bold",
                                    "size": "sm",
                                    "align": "end",
                                    "gravity": "center"
                                },
                                {
                                    "type": "text",
                                    "text": btc[1],
                                    "color": "#111111",
                                    "weight": "bold",
                                    "size": "sm",
                                    "align": "end",
                                    "gravity": "center"
                                },
                                {
                                    "type": "text",
                                    "text": btc[2],
                                    "color": "#111111",
                                    "weight": "bold",
                                    "size": "sm",
                                    "align": "end",
                                    "gravity": "center"
                                }
                                ]
                            },
                            {
                                "margin": "md",
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "image",
                                    "url": "https://assets.coingecko.com/coins/images/279/small/ethereum.png?1595348880",
                                    "aspectRatio": "120:48"
                                },
                                {
                                    "type": "text",
                                    "text": eth[0],
                                    "color": "#111111",
                                    "weight": "bold",
                                    "size": "sm",
                                    "align": "end",
                                    "gravity": "center"
                                },
                                {
                                    "type": "text",
                                    "text": eth[1],
                                    "color": "#111111",
                                    "weight": "bold",
                                    "size": "sm",
                                    "align": "end",
                                    "gravity": "center"
                                },
                                {
                                    "type": "text",
                                    "text": eth[2],
                                    "color": "#111111",
                                    "weight": "bold",
                                    "size": "sm",
                                    "align": "end",
                                    "gravity": "center"
                                }
                                ]
                            },
                            {
                                "margin": "md",
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "image",
                                    "url": "https://assets.coingecko.com/coins/images/780/small/bitcoin-cash-circle.png?1594689492",
                                    "aspectRatio": "120:48"
                                },
                                {
                                    "type": "text",
                                    "text": bch[0],
                                    "color": "#111111",
                                    "weight": "bold",
                                    "size": "sm",
                                    "align": "end",
                                    "gravity": "center"
                                },
                                {
                                    "type": "text",
                                    "text": bch[1],
                                    "color": "#111111",
                                    "weight": "bold",
                                    "size": "sm",
                                    "align": "end",
                                    "gravity": "center"
                                },
                                {
                                    "type": "text",
                                    "text": bch[2],
                                    "color": "#111111",
                                    "weight": "bold",
                                    "size": "sm",
                                    "align": "end",
                                    "gravity": "center"
                                }
                                ]
                            },
                            {
                                "margin": "md",
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": f"注意：價格更新時間為 {timestamp} (TimeStamp)",
                                    "weight": "bold",
                                    "color": "#999999",
                                    "size": "xxs",
                                    "flex": 1,
                                    "wrap": True
                                }
                                ]
                            }
                            ]
                        },
                        "footer": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "Source : max.maicoin.com",
                                    "color": "#999999",
                                    "size": "xs",
                                    "align": "end",
                                    "flex": 1
                                }
                                ],
                                "margin": "xs"
                            }
                            ]
                        },
                        "styles": {
                            "header": {
                            "backgroundColor": "#6486E3"
                            },
                            "body": {
                            "backgroundColor": "#FEFEFE"
                            },
                            "footer": {
                            "separator": True
                            }
                        }
                        }
                    ]
                    }
    )
    return flex_message

def flex_twd_orderbook():
    btc = get_orderbook('btctwd')
    eth = get_orderbook('ethtwd')
    bch = get_orderbook('bchtwd')
    timestamp = requests.get('https://max-api.maicoin.com/api/v2/timestamp').json()

    flex_message = FlexSendMessage(
        alt_text = "MAX 台幣訂單簿",
        contents = {
                    "type": "carousel",
                    "contents": [
                        {
                        "type": "bubble",
                        "size": "giga",
                        "header": {
                            "type": "box",
                            "layout": "horizontal",
                            "backgroundColor": "#00bce4",
                            "contents": [
                            {
                                "type": "image",
                                "url": "https://www.bangchak.co.th/img/logo.png",
                                "aspectRatio": "137:40",
                                "size": "md",
                                "align": "start"
                            },
                            {
                                "type": "text",
                                "weight": "bold",
                                "size": "md",
                                "gravity": "center",
                                "align": "end",
                                "color": "#FFFFFF",
                                "text": "Max 台幣訂單簿"
                            }
                            ]
                        },
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "margin": "md",
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "filler"
                                },
                                {
                                    "type": "text",
                                    "text": "買一",
                                    "color": "#111111",
                                    "weight": "bold",
                                    "size": "sm",
                                    "align": "end"
                                },
                                {
                                    "type": "text",
                                    "text": "賣一",
                                    "color": "#111111",
                                    "weight": "bold",
                                    "size": "sm",
                                    "align": "end"
                                },
                                {
                                    "type": "text",
                                    "text": "最新",
                                    "size": "sm",
                                    "color": "#111111",
                                    "weight": "bold",
                                    "align": "end"
                                }
                                ]
                            },
                            {
                                "type": "separator",
                                "color": "#cccccc",
                                "margin": "md"
                            },
                            {
                                "margin": "md",
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "image",
                                    "url": "https://assets.coingecko.com/coins/images/1/small/bitcoin.png?1547033579",
                                    "aspectRatio": "120:48"
                                },
                                {
                                    "type": "text",
                                    "text": btc[0],
                                    "color": "#111111",
                                    "weight": "bold",
                                    "size": "sm",
                                    "align": "end",
                                    "gravity": "center"
                                },
                                {
                                    "type": "text",
                                    "text": btc[1],
                                    "color": "#111111",
                                    "weight": "bold",
                                    "size": "sm",
                                    "align": "end",
                                    "gravity": "center"
                                },
                                {
                                    "type": "text",
                                    "text": btc[2],
                                    "color": "#111111",
                                    "weight": "bold",
                                    "size": "sm",
                                    "align": "end",
                                    "gravity": "center"
                                }
                                ]
                            },
                            {
                                "margin": "md",
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "image",
                                    "url": "https://assets.coingecko.com/coins/images/279/small/ethereum.png?1595348880",
                                    "aspectRatio": "120:48"
                                },
                                {
                                    "type": "text",
                                    "text": eth[0],
                                    "color": "#111111",
                                    "weight": "bold",
                                    "size": "sm",
                                    "align": "end",
                                    "gravity": "center"
                                },
                                {
                                    "type": "text",
                                    "text": eth[1],
                                    "color": "#111111",
                                    "weight": "bold",
                                    "size": "sm",
                                    "align": "end",
                                    "gravity": "center"
                                },
                                {
                                    "type": "text",
                                    "text": eth[2],
                                    "color": "#111111",
                                    "weight": "bold",
                                    "size": "sm",
                                    "align": "end",
                                    "gravity": "center"
                                }
                                ]
                            },
                            {
                                "margin": "md",
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "image",
                                    "url": "https://assets.coingecko.com/coins/images/780/small/bitcoin-cash-circle.png?1594689492",
                                    "aspectRatio": "120:48"
                                },
                                {
                                    "type": "text",
                                    "text": bch[0],
                                    "color": "#111111",
                                    "weight": "bold",
                                    "size": "sm",
                                    "align": "end",
                                    "gravity": "center"
                                },
                                {
                                    "type": "text",
                                    "text": bch[1],
                                    "color": "#111111",
                                    "weight": "bold",
                                    "size": "sm",
                                    "align": "end",
                                    "gravity": "center"
                                },
                                {
                                    "type": "text",
                                    "text": bch[2],
                                    "color": "#111111",
                                    "weight": "bold",
                                    "size": "sm",
                                    "align": "end",
                                    "gravity": "center"
                                }
                                ]
                            },
                            {
                                "margin": "md",
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": f"注意：價格更新時間為 {timestamp} (TimeStamp)",
                                    "weight": "bold",
                                    "color": "#999999",
                                    "size": "xxs",
                                    "flex": 1,
                                    "wrap": True
                                }
                                ]
                            }
                            ]
                        },
                        "footer": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "Source : max.maicoin.com",
                                    "color": "#999999",
                                    "size": "xs",
                                    "align": "end",
                                    "flex": 1
                                }
                                ],
                                "margin": "xs"
                            }
                            ]
                        },
                        "styles": {
                            "header": {
                            "backgroundColor": "#6486E3"
                            },
                            "body": {
                            "backgroundColor": "#FEFEFE"
                            },
                            "footer": {
                            "separator": True
                            }
                        }
                        }
                    ]
                    }
    )
    return flex_message