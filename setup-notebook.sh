#!/bin/bash

# Print the hostname, we'll need this to connect locally
echo "You are logged into $(hostname)"
echo ""

# Define the directories we have lost track of (starting from the current directory)
REPO_DIR=$(pwd)
SWIFT_DIR=$REPO_DIR/swiftsim

# Activate the python virtual environment
source $REPO_DIR/venv/bin/activate

# Boot up a jupyter notebook in the notebooks directory and run it in the
# background reporting the url to connect to
NOTEBOOK_DIR=$REPO_DIR/notebooks
echo "Starting a jupyter notebook server in $NOTEBOOK_DIR"
jupyter notebook --ip='*' --port=8888 --no-browser --notebook-dir=$NOTEBOOK_DIR
