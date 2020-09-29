import requests, pyimgur, os

import pandas as pd

import mplfinance as mpl

from linebot.models import *

def img_klines(client, pair, limit = 100, period = 240, timestamp=None):
    df = pd.DataFrame(client.get_public_k_line(pair, limit, period, timestamp), columns=['date', 'open', 'high', 'low', 'close', 'volume'])
    df.date = pd.to_datetime(df.date, unit = 's')
    df.set_index("date", inplace=True)
    savefig = '/app/static/img/' + pair + '.png'
    mpl.plot(df, type = 'candle', style = 'binance', volume = True, mav = 10, title = pair.upper(), savefig = savefig)
    CLIENT_ID = '07f1098efd49fcb'
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(savefig, title="Uploaded with PyImgur")
    return ImageSendMessage(
                original_content_url = uploaded_image.link,
                preview_image_url = uploaded_image.link
            )