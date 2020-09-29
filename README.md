# Hi-Blockchain

## Requirement

    flask
    numpy
    pandas
    pyimgur
    gunicorn
    requests
    matplotlib
    mplfinance
    line-bot-sdk

## Buildpack

    1. heroku/python
    2. numrut/ta-lib

## Tree

    │  app.py # Flask 框架，用於 Message API Webhook
    │  Procfile # Heroku 設定
    │  requirements.txt # Python 套件
    │
    ├─.fonts # 字體
    │      msyh.ttc
    │      msyhbd.ttc
    │      msyhl.ttc
    │
    ├─API_Package # 各大交易所 API 封裝
    │  ├─FTX
    │  │      client.py
    │  │      constants.py
    │  │      helpers.py
    │  │      __init__.py
    │  │
    │  └─max
    │          client.py
    │          constants.py
    │          helpers.py
    │          __init__.py
    │
    ├─MSG_Template # 訊息模板
    │  ├─flex
    │  │      orderbook.py # 訂單簿
    │  │
    │  ├─image
    │  │      btcvix.py # 恐慌指數圖
    │  │      kline.py # K線
    │  │
    │  └─text
    │          address.py # 乙太坊、比特幣地址查詢
    │          btcvix.py # 恐慌指數
    │          coin.py # 查詢幣價
    │          gas.py # Gas 平均價格
    │          index.py # 指標運算
    │          usdt.py # USDT 匯率
    │
    ├─static
    │  ├─css
    │  │      style.css
    │  │
    │  └─img
    │          btcusdt.png
    │
    └─templates
            home.html