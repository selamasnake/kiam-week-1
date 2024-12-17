import  utils as util
import talib
import pynance.data as data

def calculate_technical_indicators(data):
    ##Simple Moving Average
    data['SMA'] = talib.SMA(data['close'], timeperiod=50)

    ##Exponential Moving Average
    data['EMA'] = talib.EMA(data['close'], timeperiod=50)

    ##Relative Strength Index
    data['RSI'] = talib.RSI(data['close'], timeperiod=50)

    # ##MACD (Moving Average Convergence Divergence)
    # macd, macdsignal = talib.MACD(data['Close'], signalperiod=50)
    # data['MACD'] = macd

# def calculate_daily_returns(data):
#     data['daily returns'] = data['close'].pct_change()
#     data = data.dropna(subset=['daily returns'])



