import pandas as pd
import numpy as np

def MACD_Crossover(df):
    short_long = np.where(df["MACD"] > df["Signal"], 1.0 , 0.0)
    df["buy_sell_signal"] = np.insert(np.diff(short_long) , 0,np.nan)
    return df

def MACD_Zerocross(df):
    trend = np.where(df["MACD"] > 0 ,1.0 , 0.0) 
    df["buy_sell_signal"] = np.insert(np.diff(trend) , 0,np.nan)
    return df

def MACD_Histogram(df):
    trend = np.where(df["Histogram"] > 0 ,1.0 , 0.0) 
    difference = np.where(df["Histogram"].diff() > 0 ,1.0 , 0.0)
    df["buy_sell_signal"] = np.negative(trend - difference)
    return df

def RSI(df,overbought=70,oversold=30):
    df["sell_signal"] = np.where(df["RSI"] > overbought , -1.0 , 0.0)
    df["sell_signal"] = df["sell_signal"].diff()
    df.loc[df["sell_signal"] == 1 , "sell_signal"] = 0.0
    
    df["buy_signal"] = np.where(df["RSI"] < oversold , 1.0 , 0.0)
    df["buy_signal"] = df["buy_signal"].diff()
    df.loc[df["buy_signal"] == -1 , "buy_signal"] = 0.0
    df['buy_sell_signal'] = df["sell_signal"] + df["buy_signal"]
    return df

def ROC(df,buythreshold = 0,sellthreshold = 0): 
    df["sell_signal"] = np.where(df["ROC"] < -(sellthreshold) , -1.0 , 0.0)
    df["sell_signal"] = df["sell_signal"].diff()
    df.loc[df["sell_signal"] == 1,"sell_signal"] = 0.0
    
    df["buy_signal"] = np.where(df["ROC"] > buythreshold , 1.0 , 0.0)
    df["buy_signal"] = df["buy_signal"].diff()
    df.loc[df["buy_signal"] == -1,"buy_signal"] = 0.0
    df['buy_sell_signal'] = df["sell_signal"] + df["buy_signal"]
    return df

def Bollinger_Bands(df):
    df["sell_signal"] = np.where(df["Adj Close"] >= df["Upper Band"] , -1.0 , 0.0)
    df["sell_signal"] = df["sell_signal"].diff()
    df.loc[df["sell_signal"] == 1,"sell_signal"] = 0.0
    
    df["buy_signal"] = np.where(df["Adj Close"] <= df["Lower Band"] , 1.0 , 0.0)
    df["buy_signal"] = df["buy_signal"].diff()
    df.loc[df["buy_signal"] == -1,"buy_signal"] = 0.0
    df['buy_sell_signal'] = df["sell_signal"] + df["buy_signal"]
    return df
