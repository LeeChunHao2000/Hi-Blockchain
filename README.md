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

    │  app.py
    │  Procfile
    │  requirements.txt
    │
    ├─.fonts
    │      msyh.ttc
    │      msyhbd.ttc
    │      msyhl.ttc
    │
    ├─API_Package
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
    ├─MSG_Template
    │  ├─flex
    │  │      orderbook.py
    │  │
    │  ├─image
    │  │      btcvix.py
    │  │      kline.py
    │  │
    │  └─text
    │          address.py
    │          btcvix.py
    │          coin.py
    │          gas.py
    │          index.py
    │          usdt.py
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