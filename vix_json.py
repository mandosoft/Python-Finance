"""
K-Means clustering applied to time series data. In this project 
CBOE VIX data from 2004 to the Present is used. 

K-Means is difficult for use in quantitative finance as the signal to noise ratio is often quite low. 
However, VIX is ofte seen as a more predictable indicator so arranging price data into optimal 
centroid positions is potentially useful. 

Sentinels (#%%) at the begining are for running python files as Jupyter notebook cells 
in VSCode.

The goal here is to assess whether VIX prices exists within ranges of centroids that my be 
helpful for adjusting other trading strategies.

"""

#%%
import copy #stl for making deep copies of dataframes
import datetime
import json 

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mpl_finance #ohlc data?
import matplotlib.dates as mdates
from matplotlib.dates import(
    DateFormatter, WeekdayLocator, DayLocator, MONDAY
)

import numpy as np
import pandas as pd
import pandas_datareader.data as web 
from sklearn.cluster import KMeans

"""
Here we'll read in the JSON file and establish what data to extract from it. 
"""
#%%
with open('/Users/Thomas/Desktop/Finance_Python/vix-daily_json.json', 'r') as vix:
    data=vix.read()


df = json.load(data)


df["H/O"] = df["High"]/df["Open"]
df["L/O"] = df["Low"]/df["Open"]
df["C/O"] = df["Close"]/df["Open"]
df.drop(
        [
            "Open", "High", "Low",
            "Close", "Volume", "Adj Close"
        ],
        axis=1, inplace=True
    )

print(df)




