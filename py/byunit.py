import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from matplotlib import ticker
import matplotlib.dates as mdates
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import covid_ont
from covid_ont import dataset_read, DIR_IMAGES


def make_plot(df_plot):
    f_plot='byunit-1500x600.png'
    fig, ax = plt.subplots(figsize=(17, 7))
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlabel('')
    ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=4))
    ax.xaxis.set_major_formatter(DateFormatter("%d-%b-%Y"))
    ax.get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    df_plot.plot(ax=ax).set_title('Daily New Cases in Public Health Units with Most Cases', fontsize=18)
    fig.savefig(DIR_IMAGES + f_plot, facecolor='oldlace')

df_cases=dataset_read('Cases by PHU')
df_cases['Date']=pd.to_datetime(df_cases['Date'])
df_cases.columns=df_cases.columns.str.replace('_', ' ')
top_5=list(df_cases.mean().sort_values(ascending=False).head(6).index.drop('Total'))

df_cases_5=df_cases.drop([col for col in df_cases.columns if col not in top_5 and col!='Date'], axis=1)
df_cases_5.set_index('Date', inplace=True)

make_plot(df_cases_5)

