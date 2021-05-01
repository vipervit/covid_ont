import sys
from time import sleep
from datetime import datetime

interval=86400
# interval=10

cycle=0

if 'win32' in sys.platform:
    sys.exit('Cannot run on Windows.')

from daemon import runner
from covid_ont import F_DEPLOY_LOG
from covid_ont.deploy import deploy, test_deploy

def log(msg):
    with open(F_DEPLOY_LOG, 'w') as f:
        f.write('{}\n{}'.format(msg, datetime.now().strftime('%d-%b %H:%M%:%S')))

def execute():
    while True:
         deploy()
         cycle += 1
         log('Cycle: ' + cycle)
         sleep(interval)

runner.DaemonRunner(execute()).do_action()
