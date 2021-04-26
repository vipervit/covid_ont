#!/bin/bash
echo "Getting latest data...."
python ~/DEV/ds/advanced/covid_ont/prod/getdata.py
echo "Making images...."
python ~/DEV/ds/advanced/covid_ont/prod/vaccases.py
python ~/DEV/ds/advanced/covid_ont/prod/byunit.py
echo "Deploying...."
firebase deploy
echo "Done."