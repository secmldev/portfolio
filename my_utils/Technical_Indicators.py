"""
Returns the necessary columns for the technical indicators
"""
import pandas as pd
import numpy as np

def MACD(df,short_window = 12,long_window = 26,signal_window = 9):
    df["long MA"] = df["Adj Close"].rolling(window = long_window).mean()
    df["short MA"]= df["Adj Close"].rolling(window = short_window).mean()
    df["MACD"] = df["short MA"] - df["long MA"] 
    df["Signal"] = df["MACD"].rolling(window = signal_window).mean()  
    df["Histogram"] = df["MACD"] - df["Signal"] 
    return df

def RSI_Traditional(df , window = 14):
    df["Gain"] = df["Adj Close"].diff()
    gain_first = sum(df[:window]["Gain"][df[:window]["Gain"] >0])/ window
    loss_first = -(sum(df[:window]["Gain"][df[:window]["Gain"] <0]))/ window
    avg_gain = np.zeros(window-1) + np.nan
    avg_loss = np.zeros(window-1) + np.nan
    avg_gain = np.append(avg_gain,gain_first)
    avg_loss = np.append(avg_loss,loss_first)
    for i in range(window , len(df)):
        if (df.iloc[i]["Gain"] > 0):
            avg_gain = np.append(avg_gain, (avg_gain[-1]*(window-1)+df.iloc[i]["Gain"])/window )
            avg_loss = np.append(avg_loss, (avg_loss[-1]*(window-1)+ 0 )/window )

        else:
            avg_gain = np.append(avg_gain, (avg_gain[-1]*(window-1)+0)/window )
            avg_loss = np.append(avg_loss, (avg_loss[-1]*(window-1) - df.iloc[i]["Gain"])/window )
    RS = avg_gain / avg_loss
    RSI =  100 - (100/(1+RS))
    df["RSI"] = RSI
    return df

def RSI(df , window = 14):
    df["change"] = df["Adj Close"].diff()
    df["gain"] = df["change"]
    df.loc[ df["gain"] < 0 , ["gain"]] = 0.0
    df["loss"] = df["change"]
    df.loc[ df["loss"] > 0 , ["loss"]] = 0.0
    df["loss"] = abs(df["loss"]) 
    df["avg_gain"] = df["gain"].ewm(span = 14).mean()
    df["avg_loss"] = df["loss"].ewm(span = 14).mean()
    df["RS"] = df["avg_gain"] / df["avg_loss"] 
    df["RSI"] = 100 - (100 / (1+ df["RS"])) 
    return df

def ROC(df , window = 12):
    roc = np.zeros(window) + np.nan
    price_diff = df["Adj Close"].diff(window)
    price_shift = df["Adj Close"].shift(window)
    df["ROC"] = (price_diff / price_shift) * 100  
    return df

def Bollinger_Bands(df , window = 20 , n_std = 2):
    df["Moving Avg"] = df["Adj Close"].rolling(window = window).mean()
    deviation = n_std * df["Adj Close"].rolling(window = window).std()
    df["Lower Band"] = df["Moving Avg"] - deviation
    df["Upper Band"] = df["Moving Avg"] + deviation
    return df
        