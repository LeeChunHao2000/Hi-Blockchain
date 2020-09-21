import re, time
import requests
import pandas as pd
import matplotlib.pyplot as plt

from flask import Flask, request, abort, render_template

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

from API_Package.max.client import *

from MSG_Template.flex.orderbook import *
from MSG_Template.image.kline import *

# 全域變數
app = Flask(__name__)
# 基本設定
line_bot_api = LineBotApi(
    'fxd8HPifCKjpGVCC6xMLkb1XZjkte0iFkEMXgbaZ7vY3K49qMprpRSR2fdr3Ez3dJ61ytRQ7Z/yQne2yugEAMUWtNmt8FhMpcO0sc6Dm9xBfAO1uym20V3RcDPSC0NaBaBkRWbxRkFpNC8SLtFSYIQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('99f277290ebf0a849f4d4b32ae3d192b')

# Pandas 設定
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth', 100)
pd.set_option('display.width', 5000)
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

@app.route("/")
def home():
    timestamp = int(time.time())
    return render_template('home.html', TimeStamp=timestamp, Status='Success')

# 監聽所有來自 /callback 的 Post Request


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    user_id = event.source.user_id
    # ================================

if __name__ == "__main__":
    app.run()