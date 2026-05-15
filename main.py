from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
import urllib.request, json
import os
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler

data_source = 'kaggle'

if data_source == 'alphavantage':
    # AlphaVantage code here
    pass

else:
    df = pd.read_csv(
        os.path.join('Stocks', 'hpq.us.txt'),
        delimiter=',',
        usecols=['Date','Open','High','Low','Close']
    )

    print('Loaded data from the Kaggle repository')
    print(df.head())