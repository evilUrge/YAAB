#!/bin/ bash
echo "Creating python virtual env"
virtualenv .env && source .env/bin/activate

echo "Setting up env params"
set -e
export PYTHONPATH=$pwd

echo "Installing requirements"
pip install -r requirements.txt

echo "Initiate test suite"
test=true py.test tests/*.py --junitxml=automation.xml --html=automation.html

echo "fin"
