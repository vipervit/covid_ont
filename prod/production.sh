#!/bin/bash
echo "Getting latest data...."
python prod/getdata.py
echo "Making images...."
python prod/vaccases.py
python prod/byunit.py
echo "Deploying...."
firebase deploy
echo "Done."
