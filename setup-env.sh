#!/bin/bash

# This script sets up the environment for the ExGal-SPH workshop.

# Request a thread to work on with the notebook
echo "Requesting a thread to work on with the notebook: srun -p dine2 -A do020 -t 01:30:00 -n 1 --pty /bin/bash"
srun -p dine2 -A do020 -t 01:30:00 -n 1 --pty /bin/bash

# Load the necessary modules
echo "Loading necessary modules..."
echo "Running: module load intel_comp/2024.2.0 compiler-rt tbb compiler mpi ucx/1.17.0 parallel_hdf5/1.14.4 fftw/3.3.10 parmetis/4.0.3-64bit gsl/2.8 python/3.12.4"
module load intel_comp/2024.2.0 compiler-rt tbb compiler mpi ucx/1.17.0 parallel_hdf5/1.14.4 fftw/3.3.10 parmetis/4.0.3-64bit gsl/2.8 python/3.12.4
module list
echo ""

# Activate the python virtual environment
source $REPO_DIR/venv/bin/activate

# Boot up a jupyter notebook in the notebooks directory and run it in the
# background reporting the url to connect to
NOTEBOOK_DIR=$REPO_DIR/notebooks
echo "Starting a jupyter notebook server in $NOTEBOOK_DIR"
nohup jupyter notebook --ip='*' --port=8888 --no-browser --allow-root --notebook-dir=$NOTEBOOK_DIR
