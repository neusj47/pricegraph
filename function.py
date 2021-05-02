# Ticker별 데이터를 가져오는 함수

import datetime
import pandas_datareader.data as web

ticker = 'MSFT'

def get_price_from_yahoo(ticker):
    start = datetime.datetime(2020, 1, 1)
    end = datetime.datetime.now()
    df = web.DataReader(ticker, 'yahoo', start, end)
    df.reset_index(inplace=True)
    df.set_index('Date', inplace=True)
    return df