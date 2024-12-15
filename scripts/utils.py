import pandas as pd 

def read_csv_drive(url):
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
    data['date'] = pd.to_datetime(data['date'], format='ISO8601')

def drop_unnamed_column(data):
    # data = data.loc[:, ~data.columns.str.contains('^Unnamed')]
    data = data.drop(columns=['Unnamed: 0'])
    return data.head(5)