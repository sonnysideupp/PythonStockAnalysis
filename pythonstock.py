import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style 
import pandas as pd
import pandas_datareader.data as web
import fix_yahoo_finance as yf
from pandas.plotting import lag_plot
from pandas.plotting import autocorrelation_plot
from pandas import DataFrame
from pandas import concat
import numpy as np
style.use('ggplot')
start = dt.datetime(2000,1,1)
end = dt.datetime(2018,12,31)



df = yf.download('^GSPC','2016-01-01','2018-01-01')
adjusted = df['Adj Close']
volume = df['Volume']
df['Return'] = np.array([0]*len(AAPL))
for i in range(1,len(df.Return)):
    df.loc[df.index[i],['Return']] = (df['Adj Close'][i]/df['Adj Close'][i-1]) - 1
series = df['Return']
lag_plot(series)
autocorrelation_plot(series)
plt.show()
values = DataFrame(series.values)
series = concat([values.shift(1), values], axis=1)
series.columns = ['t-1', 't+1']
result = series.corr()
print(result)

df['100ma'] = df['Adj Close'].rolling(window = 100, min_periods= 0).mean()
ax1 = plt.subplot2grid((6,1),(0,0),rowspan = 5, colspan= 1)
ax2 = plt.subplot2grid((6,1),(5,0),rowspan = 1, colspan= 1,sharex = ax1)

ax1.plot(adjusted)
ax1.plot(df['100ma'])
ax2.plot(df['Volume'])
plt.show()