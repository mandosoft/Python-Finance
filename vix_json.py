"""
K-Means clustering applied to time series data. In this project 
CBOE VIX data from 2004 to the Present is used. 

Sentinels (#%%) at the begining are for running python files as Jupyter notebook cells 
in VSCode.

"""

#%%
from time import time
import numpy as np
import matplotlib.pyplot as plt
import json
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
#%%

with open('/Users/Thomas/Desktop/Finance_Python/vix-daily_json.json', 'r') as vix:
    data=vix.read()
obj = json.loads(data)
print(obj[])




