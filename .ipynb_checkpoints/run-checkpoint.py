import sys
from time import sleep

if 'win32' in sys.platform:
    sys.exit('Cannot run on Windows.')

from daemon import runner
from covid_ont.deploy import deploy
def run():
    while True:
         deploy()
         sleep(86400)
drunner=runner.DaemonRunner(run())
runner.do_action()
