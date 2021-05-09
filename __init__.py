import os
import pandas as pd

__version__='1.15.03'

DIR_ROOT = __file__.split('__init__')[0]
DIR_DATA = ''.join([DIR_ROOT, 'data', os.sep])
DIR_SITE = ''.join([DIR_ROOT, 'site', os.sep])
DIR_IMAGES = ''.join([DIR_SITE, 'assets', os.sep, 'images', os.sep])
DIR_LOG = DIR_ROOT
FNAME_DEPLOY_LOG = 'deploy.log'
F_DEPLOY_LOG = ''.join([DIR_ROOT, os.sep, FNAME_DEPLOY_LOG])

FIGSIZES=(17,7)

SRC = {
    'Vaccinations':
        {'url': 'https://data.ontario.ca/dataset/752ce2b7-c15a-4965-a3dc-397bf405e7cc/resource/8a89caa9-511c-4568-af89-7f2174b4378c/download/vaccine_doses.csv',
         'pickle': 'vaxxs'},
    'Cases by PHU':
        {'url': 'https://data.ontario.ca/dataset/f4f86e54-872d-43f8-8a86-3892fd3cb5e6/resource/8a88fe6d-d8fb-41a3-9d04-f0550a44999f/download/daily_change_in_cases_by_phu.csv',
         'pickle': 'byphu'},
    'Cases & Tests':
        {'url': 'https://data.ontario.ca/dataset/f4f86e54-872d-43f8-8a86-3892fd3cb5e6/resource/ed270bb8-340b-41f9-a7c6-e8ef587e6d11/download/covidtesting.csv',
         'pickle': 'casets'}
}

def dataset_read(source_name):
    return pd.read_pickle(DIR_DATA + SRC[source_name]['pickle'] + '.pkl')

def dataset_get(source_name):
    return pd.read_csv(SRC[source_name]['url']).to_pickle(DIR_DATA + SRC[source_name]['pickle'] + '.pkl')
