import subprocess
from covid_ont import DIR_LOG

def deploy():
    print('Downloading data...')
    from covid_ont.py import getdata
    print('Making plots...')
    from covid_ont.py import vaccases
    from covid_ont.py import byunit
    print('Deploying...')
    subprocess.run(['firebase', 'deploy'])
    print('Done.')
