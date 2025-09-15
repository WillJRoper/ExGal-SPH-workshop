#!/bin/bash

# This script sets up the environment and your directory for the ExGal-SPH workshop.

# Clone the repo to the directory passed as an argument
REPO_DIR=$1
echo "Cloning the ExGal-SPH-workshop repository into $REPO_DIR"
git clone https://github.com/WillJRoper/ExGal-SPH-workshop.git $REPO_DIR
echo ""

# Load the necessary modules
echo "Loading necessary modules..."
echo "Running: module load intel_comp/2024.2.0 compiler-rt tbb compiler mpi ucx/1.17.0 parallel_hdf5/1.14.4 fftw/3.3.10 parmetis/4.0.3-64bit gsl/2.8 python/3.12.4"
module load intel_comp/2024.2.0 compiler-rt tbb compiler mpi ucx/1.17.0 parallel_hdf5/1.14.4 fftw/3.3.10 parmetis/4.0.3-64bit gsl/2.8 python/3.12.4
module list
echo ""

# Clone SWIFT
SWIFT_DIR=$REPO_DIR/swiftsim
echo "Cloning SWIFT into $SWIFT_DIR"
git clone https://gitlab.cosma.dur.ac.uk/swift/swiftsim.git $SWIFT_DIR
cd $SWIFT_DIR
echo ""
./autogen.sh
echo ""
cd -

# Download EAGLE data dependencies incase we use them
echo "Downloading EAGLE data dependencies..."
cd $REPO_DIR
$SWIFT_DIR/examples/EAGLE_ICs/getEagleCoolingTable.sh
$SWIFT_DIR/examples/EAGLE_ICs/getEaglePhotometryTable.sh
$SWIFT_DIR/examples/EAGLE_ICs/getEagleYieldTable.sh
$SWIFT_DIR/examples/EAGLE_ICs/getPS2020CoolingTables.sh
cd -

# Export some helpful environment variables to automate things later
export SWIFT_DIR
export PATH=$SWIFT_DIR/$PATH
