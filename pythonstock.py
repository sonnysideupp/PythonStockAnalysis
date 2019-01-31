import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style 
import pandas as pd
import pandas_datareader.data as web
import fix_yahoo_finance as yf



style.use('ggplot')
start = dt.datetime(2000,1,1)
end = dt.datetime(2018,12,31)



df = yf.download('AAPL','2016-01-01','2018-01-01')
adjusted = df['Adj Close']
volume = df['Volume']
df['Return'] = df['Close'] - df['Open']

df['100ma'] = df['Adj Close'].rolling(window = 100, min_periods= 0).mean()
ax1 = plt.subplot2grid((6,1),(0,0),rowspan = 5, colspan= 1)
ax2 = plt.subplot2grid((6,1),(5,0),rowspan = 1, colspan= 1,sharex = ax1)

ax1.plot(adjusted)
ax1.plot(df['100ma'])
ax2.plot(df['Volume'])
plt.show()