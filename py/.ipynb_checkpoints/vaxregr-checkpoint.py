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
from sklearn.linear_model import LinearRegression, Ridge, RidgeCV
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
import numpy as np

sys.path.append(os.getenv('DEV_HOME'))
sys.path.append(os.getenv('SITES_HOME'))

import covid_ont
from covid_ont import dataset_read, dataset_get, DIR_IMAGES, FIGSIZES

f_plot='vaxxregr.png'

ontario_pop_estimate=14755211 # Q1 2021, source: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710000901
forecast_depth=300

df=dataset_read('Vaccinations')
df.columns=['Date', 'Previous Day Doses Administered', 'Total Doses', 'Total Doses in Fully Vaccinated', 'Total Fully Vaccinated']
df.fillna(0, inplace=True)
df.set_index('Date', inplace=True)
df=df.astype(int)
df.index=pd.to_datetime(df.index)
df.insert(column='Percentage of Population Vaccinated with One Dose', loc=2, value=0)
df.insert(column='Percentage of Population Fully Vaccinated', loc=5, value=0)

df['Percentage of Population Vaccinated with One Dose']= df['Total Doses'].apply(lambda x: x*100/ontario_pop_estimate)
df['Percentage of Population Fully Vaccinated'] = df['Total Fully Vaccinated'].apply(lambda x: x*100/ontario_pop_estimate)

df_future=df.append(pd.DataFrame([[0,0,0,0,0,0] for i in range(forecast_depth)], index=pd.date_range(start=df.index.max(), periods=forecast_depth, freq='D'), columns=df.columns))

X_act=np.reshape(df.index, (-1,1)) 
y_act=df['Percentage of Population Vaccinated with One Dose']

X_train, X_test, y_train, y_test = train_test_split(X_act, y_act, test_size=0.8, random_state=42)

pipe=make_pipeline(PolynomialFeatures(degree=6), Ridge())
pipe.fit(X_train, y_train).score(X_test, y_test)
yhat=pipe.predict(X_act)

# Prediction

df_pred=df_future.loc[df_future.index>df.index.max()][['Percentage of Population Vaccinated with One Dose']]

X_pred=np.reshape(df_pred.index, (-1,1))
y_pred=pipe.predict(X_pred)

df_pred['Percentage of Population Vaccinated with One Dose']=y_pred
df_pred=df_pred[df_pred['Percentage of Population Vaccinated with One Dose']<100]
df_plot_pred=df_pred.copy()
df_plot_pred.columns=['Projection']

df_plot_act=df.copy()[['Percentage of Population Vaccinated with One Dose']]
df_plot_act.columns=['Actual']

peak=df_plot_pred[df_plot_pred.index==df_plot_pred.index.max()]
sevfive=df_plot_pred[df_plot_pred['Projection'].between(74, 76)]
fifty=df_plot_pred[df_plot_pred['Projection'].between(49,51)]
today=df_plot_act[df_plot_act.index==df_plot_act.index.max()]

# Plot
arrowprops={'arrowstyle': '->', 'color': 'blue', 'lw': 4, 'ls': 'dashed'}
labels=['Actual', 'Projection']
plt.figure(figsize=FIGSIZES)
plt.title('Percentage of Population Vaccinated with At Least One Dose', fontsize=15)
ax=sns.lineplot(data=df_plot_act, palette=['red'], linewidth=4)
sns.lineplot(data=df_plot_pred, palette=['blue'], linewidth=4)
ax.set_xlabel('')
plt.xlim(df_plot_act.index[0], df_pred.index.max())
plt.legend(loc='best')
plt.ylim(0, 110)
plt.grid()

plt.text(df_plot_act.index.mean(), peak['Projection']+5, peak.index[0].strftime('%d-%b-%Y'), color='blue', fontsize=12)
plt.text(df_plot_act.index.mean(), today['Actual']+5, today.index[0].strftime('%d-%b-%Y'), color='red', fontsize=12)

ax.hlines(today['Actual'], df_plot_act.index[0], today.index[0], linestyles='dashed', color='red')
ax.hlines(peak['Projection'], df_plot_act.index.min(), df_plot_pred.index.max(), linestyles='dashed', color='blue')

plt.vlines(today.index[0], today['Actual'], 0, linestyles='dashed', color='red')

plt.savefig(DIR_IMAGES + f_plot, facecolor='oldlace')

