import pandas as pd 
import os

def load_data_drive(url):
    file_id=url.split('/')[-2]
    dwn_url='https://drive.google.com/uc?id=' + file_id
    data = pd.read_csv(dwn_url)
    pd.set_option('display.max_columns', 15)
    return data

def load_data(filepath):
    pd.set_option('display.max_columns', 15)
    data = pd.read_csv(filepath)
    return data

def explore_data(data):
    print("Shape of the data:", data.shape)
    print("Info of the data:", data.info())

# def check_datatypes(data):
#     return data.dtypes

def convert_date_dtype(data):
    data['date'] = pd.to_datetime(data['date'], 'coerce')

def drop_unnamed_column(data):
    # data = data.loc[:, ~data.columns.str.contains('^Unnamed')]
    data = data.drop(columns=['Unnamed: 0'])
    return data.head(5)

##Stock

def extract_ticker(file_path):
    filename = os.path.basename(file_path)
    ticker = filename.split('_')[0] 
    return ticker

def load_stock_data(file_path):
    ticker = extract_ticker(file_path)
    data = pd.read_csv(file_path)
    data.insert(0, 'Ticker', ticker)
    return data

def index_by_date(data):
    data['date'] = pd.to_datetime(data['date'], 'coerce')
    data.set_index('date', inplace=True)

def filter_data_by_stock(data, ticker):
    filtered_data = data[data['stock'] == ticker]
    return filtered_data

def reset_index(data):
    data = data.reset_index(drop=True)