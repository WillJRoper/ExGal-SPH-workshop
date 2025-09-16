#!/bin/bash

# Set up the python environment
module load python/3.12.4
python -m venv sph-env
source sph-env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
deactivate
