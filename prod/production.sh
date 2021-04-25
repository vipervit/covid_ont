#!/bin/bash
echo "Getting latest data...."
python covid_ont/prod/getdata.py
echo "Making images...."
python covid_ont/prod/vaccases.py
python covid_ont/prod/byunit.py
echo "Deploying...."
firebase deploy
echo "Done."
