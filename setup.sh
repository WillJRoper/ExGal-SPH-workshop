#!/bin/bash

# This script sets up the environment and your directory for the ExGal-SPH workshop.

# Clone the repo to the directory passed as an argument
REPO_DIR=$1
echo "Cloning the ExGal-SPH-workshop repository into $REPO_DIR"
git clone https://github.com/WillJRoper/ExGal-SPH-workshop.git $REPO_DIR

# Load the necessary modules
echo "Loading necessary modules..."

# Clone SWIFT
SWIFT_DIR=$REPO_DIR/swiftsim
echo "Cloning SWIFT into $SWIFT_DIR"
git clone https://gitlab.cosma.dur.ac.uk/swift/swiftsim.git $SWIFT_DIR

# Download EAGLE data dependencies incase we use them
echo "Downloading EAGLE data dependencies..."
$SWIFT_DIR/examples/EAGLE_ICs/getEagleCoolingTable.sh
$SWIFT_DIR/examples/EAGLE_ICs/getEaglePhotometryTable.sh
$SWIFT_DIR/examples/EAGLE_ICs/getEagleYieldTable.sh
$SWIFT_DIR/examples/EAGLE_ICs/getPS2020CoolingTables.sh
