#!/usr/bin/env python

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
from ds.advanced.covid_ont import dataset_read, DIR_IMAGES

f_plot='vaccases-1700x600.png'

df_cases=dataset_read('Cases by PHU')[['Date', 'Total']]
df_cases.columns=['Date', 'New Cases']                 
df_vac=dataset_read('Vaccinations')[['report_date', 'total_individuals_fully_vaccinated']]
df_vac.columns=['Date', 'Fully Vaccinated Total']

df_plot=pd.merge(df_vac, df_cases, on='Date')
df_plot['Fully Vaccinated Total']=df_plot['Fully Vaccinated Total'].str.replace(',', '')
df_plot.fillna(0, inplace=True)
df_plot['Fully Vaccinated Total']=df_plot['Fully Vaccinated Total'].astype(int)
df_plot.drop(df_plot[df_plot['Fully Vaccinated Total']==0].index, inplace=True)
df_plot['Date']=pd.to_datetime(df_plot['Date'])
df_plot.set_index('Date', inplace=True)

fig, ax1 = plt.subplots(1, 1, figsize=(17,6))

plt.style.use(['fast'])
ax2=ax1.twinx()
df_plot.plot(ax=ax1, kind='area', alpha=0.8, y='New Cases', color='red', label='New Cases')
df_plot.plot(ax=ax2, kind='area', alpha=0.5, y='Fully Vaccinated Total', color='green', label='Fully Vaccinated')
ax1.set_xlabel('')
ax1.set_ylabel('Cases', fontsize=20)
ax2.set_ylabel('Vaccinations', fontsize=20)
ax1.legend(loc=0)
ax2.legend(loc=4)
ax1.spines['left'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax2.spines['bottom'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax1.xaxis.set_major_locator(mdates.WeekdayLocator(interval=2))
ax1.xaxis.set_major_formatter(DateFormatter("%d-%b-%Y"))
ax1.annotate(str(df_plot.index.min().strftime('%d-%b-%Y')), xy=(0, -18), xycoords='axes points', color='black', fontsize=13)
ax1.annotate(str(df_plot.index.max().strftime('%d-%b-%Y')), xy=(945, -18), xycoords='axes points', color='red', fontsize=13)
plt.title('Vaccinations vs. New cases', fontsize=20)

fig.savefig(DIR_IMAGES + f_plot)
