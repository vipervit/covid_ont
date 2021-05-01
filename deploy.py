import subprocess
import sys
import covid_ont
from covid_ont import DIR_LOG, DIR_SITE

def deploy():
    if len(DIR_SITE)==0:
        sys.exit('Could not get site location. Make sure \'SITE_HOME\' environment variable is set up.')
    print('Downloading data...')
    from covid_ont.py import getdata
    print('Making plots...')
    from covid_ont.py import vaccases
    from covid_ont.py import byunit
    print('Deploying...')
    subprocess.run(['firebase', 'deploy'])
    print('Done.')

def test_deploy():
    return 'test_deploy says hi'

if __name__ == '__main__':
    deploy()
