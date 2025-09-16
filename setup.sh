#!/bin/bash

# This script sets up your directory structure for the ExGal-SPH workshop and downloads some dependent data.

# Clone SWIFT
REPO_DIR=$(pwd)
SWIFT_DIR=$REPO_DIR/swiftsim
echo "Cloning SWIFT into $SWIFT_DIR"
git clone https://gitlab.cosma.dur.ac.uk/swift/swiftsim.git $SWIFT_DIR
cd $SWIFT_DIR
echo ""
./autogen.sh
echo ""
cd -
echo ""

# Set up the python environment
module load python/3.12.4
python -m venv $REPO_DIR/venv
source $REPO_DIR/venv/bin/activate
pip install --upgrade pip
pip install -r $REPO_DIR/requirements.txt
deactivate
echo ""

cd $REPO_DIR
