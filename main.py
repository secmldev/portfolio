import pandas as pd
import numpy as np
import pandas_datareader as web
import datetime as dt
import quandl
from my_utils import Read_Write_Data as rwd
from my_utils import Technical_Indicators as ti
from my_utils import Signal_Generators as sg
from my_utils import Plot_Signals as ps
from my_utils import Portfolios
import datetime as dt
import matplotlib.pyplot as plt

if __name__ == "__main__":

    print("Code Started")
    stocks = ['RELIANCE']
    for stock in stocks:
        df = rwd.get_price_yahoo(stock + ".NS")
        roc = ti.ROC(df)
        buy_sell = sg.ROC(roc, buythreshold=5, sellthreshold=5)

    portfolio = Portfolios.portfolio(signals=buy_sell, initial_capital=100000)
    portfolio_positions = portfolio.create_positions()
    portfolio.Plot_portfolio(portfolio_positions)
    print("Code End")