echo "Getting latest data...."
python py/getdata.py
echo "Making images...."
python py/vaccases.py
python py/byunit.py
echo "Deploying...."
firebase deploy
echo "Done."
