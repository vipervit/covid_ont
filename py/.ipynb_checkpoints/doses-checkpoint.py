import sys
import os
sys.path.append(os.getenv('DEV_HOME'))
sys.path.append(os.getenv('SITES_HOME'))
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.dates import DateFormatter
from matplotlib import ticker
import matplotlib.dates as mdates
import matplotlib.patches as mpatches
import warnings
warnings.filterwarnings(action='ignore')
# warnings.simplefilter(action='ignore', category=FutureWarning)

import covid_ont
from covid_ont import dataset_read, dataset_get, DIR_IMAGES, FIGSIZES

f_plot='doses-1700x700.png'

dataset_get('Vaccinations')
df_vac_src=dataset_read('Vaccinations')

df_doses=df_vac_src[['report_date','total_doses_administered', 'total_doses_in_fully_vaccinated_individuals']]
df_doses.columns=['Date', 'Doses Administered', 'Doses in Fully Vaccinated']
df_doses.fillna(0, inplace=True)
df_doses.set_index('Date', inplace=True)
df_doses.index=pd.to_datetime(df_doses.index)

fig, ax = plt.subplots(figsize=FIGSIZES)

plt.style.use('fast')

ax.bar(df_doses.index, df_doses['Doses Administered'], alpha=0.7, color='cyan')
ax.bar(df_doses.index, df_doses['Doses in Fully Vaccinated'], alpha=0.8, color='deepskyblue')
sns.despine(top=True, bottom=True, right=True, left=True)

top_bar = mpatches.Patch(color='deepskyblue', label='Doses in Fully Vaccinated')
bottom_bar = mpatches.Patch(color='cyan', label='Total Administered Doses')

ax.set_xlabel('')
ax.set_ylabel('')
ax.get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=4))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b-%Y'))

plt.legend(handles=[top_bar, bottom_bar])
plt.title('Vaccinations', fontsize=18)

plt.savefig(DIR_IMAGES + f_plot, facecolor='oldlace')

