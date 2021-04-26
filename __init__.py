import pandas as pd
import os

DIR_ROOT=os.getcwd()
DIR_DATA = ''.join([DIR_ROOT, os.sep, 'data', os.sep])
DIR_SITE = ''.join([DIR_ROOT, os.sep, 'site', os.sep])
DIR_IMAGES = ''.join([DIR_SITE, os.sep, 'assets', os.sep, 'images', os.sep])

SRC = {
    'Vaccinations':
        {'url': 'https://data.ontario.ca/dataset/752ce2b7-c15a-4965-a3dc-397bf405e7cc/resource/8a89caa9-511c-4568-af89-7f2174b4378c/download/vaccine_doses.csv',
         'pickle': 'vaxxs'},
    'Cases by PHU':
        {'url': 'https://data.ontario.ca/dataset/f4f86e54-872d-43f8-8a86-3892fd3cb5e6/resource/8a88fe6d-d8fb-41a3-9d04-f0550a44999f/download/daily_change_in_cases_by_phu.csv',
         'pickle': 'cases'}
}

def dataset_read(source_name):
    return pd.read_pickle(DIR_DATA + SRC[source_name]['pickle'] + '.pkl')

def dataset_get(source_name):
    return pd.read_csv(SRC[source_name]['url']).to_pickle(DIR_DATA + SRC[source_name]['pickle'] + '.pkl')
