import pandas as pd
import matplotlib.pyplot as plt
from covid_ont import dataset_read, DIR_IMAGES

f_plot='byunit-1500x600.png'

df_cases=dataset_read('Cases by PHU')
df_cases['Date']=pd.to_datetime(df_cases['Date'])
df_cases.columns=df_cases.columns.str.replace('_', ' ')
top_5=list(df_cases.mean().sort_values(ascending=False).head(6).index.drop('Total'))

df_cases_5=df_cases.drop([col for col in df_cases.columns if col not in top_5 and col!='Date'], axis=1)
df_cases_5.set_index('Date', inplace=True)
df_cases_5

fig, ax = plt.subplots(figsize=(15, 6))
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
df_cases_5.plot(ax=ax)

fig.savefig(DIR_IMAGES + f_plot)
