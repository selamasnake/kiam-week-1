import  utils as util
import talib
import pynance.data as data

def calculate_technical_indicators(data):
    ##Simple Moving Average
    data['SMA'] = talib.SMA(data['Close'], timeperiod=50)

    ##Exponential Moving Average
    data['EMA'] = talib.EMA(data['Close'], timeperiod=50)

    ##Relative Strength Index
    data['RSI'] = talib.RSI(data['Close'], timeperiod=50)

    ##MACD (Moving Average Convergence Divergence)
    macd, macdsignal, _ = talib.MACD(data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)

    # Add the MACD and Signal line to your DataFrame
    data['MACD'] = macd
    data['MACDSignal'] = macdsignal

def calculate_daily_returns(data):
    data['Daily Returns'] = data['Close'].pct_change()
    data = data.dropna(subset=['Daily Returns'])



