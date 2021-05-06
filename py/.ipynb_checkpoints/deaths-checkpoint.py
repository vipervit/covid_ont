import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.dates import DateFormatter
from matplotlib import ticker
import matplotlib.dates as mdates
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import numpy as np

import sys
import os
sys.path.append(os.getenv('DEV_HOME'))
sys.path.append(os.getenv('SITES_HOME'))
import covid_ont
from covid_ont import dataset_read, dataset_get, DIR_IMAGES

def make_plot(df_plot):
    f_plot='deaths'
    fig, ax1 = plt.subplots(1, 1, figsize=(17,7))
    plt.style.use('fast')
    ax2=ax1.twinx()
    df_plot.plot(ax=ax1, kind='area', alpha=0.5, y='New Cases', color='red', label='Daily Cases')
    df_plot.plot(ax=ax2, kind='area', alpha=0.5, y='Deaths', color='black', label='Daily Deaths')
    ax1.set_xlabel('')
    ax1.set_ylabel('Cases', fontsize=20)
    ax2.set_ylabel('Deaths', fontsize=20)
    ax1.legend(loc=0, bbox_to_anchor=(0.15, 1.08))
    ax2.legend(loc=1, bbox_to_anchor=(0.965, 1.08))
    ax1.spines['left'].set_visible(False)
    ax2.spines['left'].set_visible(False)
    ax1.spines['top'].set_visible(False)
    ax2.spines['top'].set_visible(False)
    ax1.spines['bottom'].set_visible(False)
    ax2.spines['bottom'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax1.xaxis.set_major_locator(mdates.WeekdayLocator(interval=4))
    ax1.xaxis.set_major_formatter(DateFormatter("%d-%b-%Y"))
    ax1.get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    ax2.get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    plt.title('Daily Deaths vs Daily Cases', fontsize=18)
    fig.savefig(DIR_IMAGES + f_plot, facecolor='oldlace')

df_cases_src=dataset_read('Cases & Tests')
df_cases_src.fillna(0, inplace=True)
df_cases_src.columns

deaths=[]
for i in range(len(df_cases_src.index)):
    prev, curr = df_cases_src['Deaths'].iloc[i-1], df_cases_src['Deaths'].iloc[i]
    if curr>prev:
        deaths.append(curr-prev)
    else:
        deaths.append(1.0)
deaths[0]=0

df_deaths=df_cases_src[['Reported Date']].rename({'Reported Date': 'Date'}, axis=1)
df_deaths.set_index('Date', inplace=True)
df_deaths['Deaths']=deaths

df_cases_daily=dataset_read('Cases by PHU')[['Date', 'Total']]
df_cases_daily.columns=['Date', 'New Cases']
df_cases_daily.set_index('Date', inplace=True)
df_cases_daily.tail()

df_plot=pd.merge(df_deaths, df_cases_daily, on='Date')
df_plot.index=pd.to_datetime(df_plot.index)

make_plot(df_plot)
