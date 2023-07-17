import pandas as pd
import pandas_datareader as web
import datetime as dt
import yfinance as yf

def read_stock_csv(folder_name, stock_name, index_col):
    """ 
    This is a method for reading stock data 
    Input Argument: 
    Folder name 
    Stock name 
    Column for indexing 
    Output: 
    Stock data with date as index 
    """ 
    file_name = folder_name + "/" + stock_name + ".csv" 
    data = pd.read_csv(file_name) 
    data[index_col] = pd.to_datetime(data[index_col])
    data = data.set_index(index_col)
    print("stock name: ", stock_name) 
    print("Stock data variables: ", data.columns) 
    print(data.head()) 
    return data

def get_price_yahoo(symbol, data_source = "yahoo",start_date="2012-01-01",end_date = dt.datetime.today()):
    data = web.DataReader(name = symbol, data_source = "yahoo", start = start_date, end = end_date)
    data.index = pd.to_datetime(data.index)
    return data

def get_stock_info_yahoo(symbol, data_source = "yahoo",start_date="2012-01-01",end_date = dt.datetime.today()):
    ticker = yf.Ticker(symbol)
    info = ticker.info 
    data = ticker.history(period = "max" , interval = "1d",start_date = start_date , end_date = end_date)
    data.index = pd.to_datetime(data.index)
    return info,data

def get_multiple_stock_info(symbols, data_source = "yahoo",start_date="2012-01-01",end_date = dt.datetime.today()):
    data = pd.DataFrame()
    data[symbols[0]] = web.DataReader(name = symbols[0], data_source = "yahoo", start = start_date, end = end_date)["Adj Close"]
    data.index = pd.to_datetime(data.index)
    for symbol in symbols[1:]:
        data[symbol] = web.DataReader(name = symbol, data_source = "yahoo", start = start_date, end = end_date)["Adj Close"]
    return data
