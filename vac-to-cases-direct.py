#!/usr/bin/env python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df_vac_src=pd.read_csv('https://data.ontario.ca/dataset/752ce2b7-c15a-4965-a3dc-397bf405e7cc/resource/8a89caa9-511c-4568-af89-7f2174b4378c/download/vaccine_doses.csv')
df_cases_src=pd.read_csv('https://data.ontario.ca/dataset/f4f86e54-872d-43f8-8a86-3892fd3cb5e6/resource/8a88fe6d-d8fb-41a3-9d04-f0550a44999f/download/daily_change_in_cases_by_phu.csv')
df_cases=df_cases_src[['Date', 'Total']]
df_cases.columns=['Date', 'New Cases']
df_vac=df_vac_src[['report_date', 'total_individuals_fully_vaccinated']]
df_vac.columns=['Date', 'Total Fully Vaccinated']
df_fully=df_vac[['Date', 'Total Fully Vaccinated']].dropna().reset_index(drop=True)
df_fully.drop(df_fully.loc[:23].index, inplace=True)
df_fully.reset_index(drop=True, inplace=True)
df_fully['Total Fully Vaccinated']=df_fully['Total Fully Vaccinated'].str.replace(',', '')
df_fully['Total Fully Vaccinated']=df_fully['Total Fully Vaccinated'].astype(int)
df_fully.fillna(0, inplace=True)
df_plot=pd.merge(df_vac, df_cases, on='Date')
df_plot['Total Fully Vaccinated']=df_plot['Total Fully Vaccinated'].str.replace(',', '')
df_plot.fillna(0, inplace=True)
df_plot['Total Fully Vaccinated']=df_plot['Total Fully Vaccinated'].astype(int)
df_plot['Total Fully Vaccinated']=df_plot['Total Fully Vaccinated'].apply(lambda x: x / 100)
plt.figure(figsize=(15,6))
sns.set_style('whitegrid')
plot=sns.lineplot(data=df_plot, palette=['green', 'red'])
plot.set_title('Vaccinations ( div. by 100) vs Daily New Cases')
plot.set_xlabel('Days since December 24, 2020')
plot.figure.savefig('plot.png')
