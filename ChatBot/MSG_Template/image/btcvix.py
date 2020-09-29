import requests

from linebot.models import *

def img_btcvix():
    return ImageSendMessage(
        original_content_url='https://alternative.me/crypto/fear-and-greed-index.png',
        preview_image_url='https://alternative.me/crypto/fear-and-greed-index.png'
        )