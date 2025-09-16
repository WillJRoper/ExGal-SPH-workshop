#!/bin/bash

# Set up the python environment
module load python/3.12.4
python -m venv sph-env
source sph-venv/bin/activate
pip install --upgrade pip
pip install -r $REPO_DIR/requirements.txt
deactivate
echo ""
