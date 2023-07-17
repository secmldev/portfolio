import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def Plot_MACD_Crossover(stock,data):
    
    buy = data[data["buy_sell_signal"] == 1].index
    sell = data[data["buy_sell_signal"] == -1].index
    # Plot single chart for last two year
    fig ,axs = plt.subplots(2,1,gridspec_kw={"height_ratios":[3,2]},sharex = True,figsize = (20,8))
    fig.suptitle(stock)
    axs[0].plot(data["Adj Close"].index ,data["Adj Close"].values,label = "Adj Close",alpha = 0.7)
    axs[0].plot(data["Adj Close"].index,data["long MA"].values,label = "Long MA",alpha = 0.5)
    axs[0].plot(data["Adj Close"].index,data["short MA"].values,label = "Short MA",alpha = 0.5)
    axs[0].scatter(buy , data.loc[buy]["Adj Close"].values , marker = "^", c =  "g" ,s = 100)
    axs[0].scatter(sell , data.loc[sell]["Adj Close"].values , marker = "v", c =  "r" ,s = 100)

    axs[0].legend()
    axs[0].grid()

    axs[1].plot(data["Adj Close"].index,data["MACD"].values,label = "MACD",alpha = 0.4)
    axs[1].plot(data["Adj Close"].index,data["Signal"].values,label = "Signal",alpha = 0.4)
    
    hist_color = np.where(data["Histogram"] > 0,"g","r")
    axs[1].bar(data["Adj Close"].index,data["Histogram"],alpha = 0.4,color = hist_color)

    axs[1].scatter(buy , data.loc[buy]["MACD"].values , marker = "^", c =  "g" ,s = 100)
    axs[1].scatter(sell , data.loc[sell]["MACD"].values , marker = "v", c =  "r" ,s = 100)

    axs[1].legend()
    axs[1].grid()

def Plot_RSI(stock,data,overbought=70,oversold=30):
    buy = data[data["buy_sell_signal"] == 1].index
    sell = data[data["buy_sell_signal"] == -1].index
    fig ,axs = plt.subplots(2,1,gridspec_kw={"height_ratios":[3,2]},sharex = True,figsize = (20,8))
    fig.suptitle(stock)
    axs[0].plot(data["Adj Close"].index ,data["Adj Close"].values,label = "Adj Close")
    axs[0].scatter(buy , data.loc[buy]["Adj Close"].values , marker = "^", c =  "g" ,s = 100)
    axs[0].scatter(sell , data.loc[sell]["Adj Close"].values , marker = "v", c =  "r" ,s = 100)
    axs[0].legend()
    axs[0].grid()
    
    axs[1].plot(data["Adj Close"].index,data["RSI"].values,label = "RSI",alpha = 0.8, c = "g")
    axs[1].axhline(overbought , ls = "--",alpha = 0.5 , c = "k")
    axs[1].axhline(oversold , ls = "--",alpha = 0.5 , c = "k" )
    axs[1].scatter(buy , data.loc[buy]["RSI"].values , marker = "^", c =  "g" ,s = 100)
    axs[1].scatter(sell , data.loc[sell]["RSI"].values , marker = "v", c =  "r" ,s = 100)
    axs[1].legend()
    axs[1].grid()
    
def Plot_ROC(stock,data):
    buy = data[data["buy_sell_signal"] == 1].index
    sell = data[data["buy_sell_signal"] == -1].index
    fig ,axs = plt.subplots(2,1,gridspec_kw={"height_ratios":[3,2]},sharex = True,figsize = (20,8))
    fig.suptitle(stock)
    axs[0].plot(data["Adj Close"].index ,data["Adj Close"].values,label = "Adj Close")
    axs[0].scatter(buy , data.loc[buy]["Adj Close"].values , marker = "^", c =  "g" ,s = 100)
    axs[0].scatter(sell , data.loc[sell]["Adj Close"].values , marker = "v", c =  "r" ,s = 100)
    
    axs[0].legend()
    axs[0].grid()
    
    axs[1].plot(data["Adj Close"].index,data["ROC"].values,label = "RSI",alpha = 0.8, c = "g")
    axs[1].scatter(buy , data.loc[buy]["ROC"].values , marker = "^", c =  "g" ,s = 100)
    axs[1].scatter(sell , data.loc[sell]["ROC"].values , marker = "v", c =  "r" ,s = 100)
    axs[1].legend()
    axs[1].grid()
    
def Plot_Bollinger_Bands(stock,data):
    buy = data[data["buy_sell_signal"] == 1].index
    sell = data[data["buy_sell_signal"] == -1].index
    fig ,axs = plt.subplots(1,1,sharex = True,figsize = (20,8))
    fig.suptitle(stock)
    for column in ['Moving Avg','Lower Band', 'Upper Band' , 'Adj Close']:
        axs.plot(data["Adj Close"].index ,data[column].values,label = column)
    
    axs.scatter(buy , data.loc[buy]["Adj Close"].values , marker = "^", c =  "g" ,s = 100)
    axs.scatter(sell , data.loc[sell]["Adj Close"].values , marker = "v", c =  "r" ,s = 100)
    
    axs.legend()
    axs.grid()
    
def Plot_Combined_Signal(stock,data):
    buy = data[data["buy_sell_signal"] == 1].index
    sell = data[data["buy_sell_signal"] == -1].index
    fig ,axs = plt.subplots(1,1,sharex = True,figsize = (20,8))
    fig.suptitle(stock)
    axs.plot(data["Adj Close"].index ,data["Adj Close"].values,label = "Adj Close")
    
    axs.scatter(buy , data.loc[buy]["Adj Close"].values , marker = "^", c =  "g" ,s = 100)
    axs.scatter(sell , data.loc[sell]["Adj Close"].values , marker = "v", c =  "r" ,s = 100)
    
    axs.legend()
    axs.grid()
    