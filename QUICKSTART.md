# Quick Start Guide

## Get Started in 5 Minutes

### 1. Clone the Repository
```bash
git clone https://github.com/WillJRoper/ExGal-SPH-workshop.git
cd ExGal-SPH-workshop
```

### 2. Set Up Python Environment
```bash
# Create virtual environment
python -m venv sph-workshop-env
source sph-workshop-env/bin/activate  # On Windows: sph-workshop-env\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

### 3. Start Jupyter Notebook
```bash
jupyter notebook
```

### 4. Open Your First Notebook
Navigate to `notebooks/` and open:
- **01_Kelvin_Helmholtz_Instability.ipynb** - Start here for fluid instabilities
- **02_Sedov_Blast_Wave.ipynb** - Classic shock wave problem  
- **03_Image_to_Hydro_Simulation.ipynb** - Turn images into simulations

## What Each Notebook Does

### Notebook 1: Kelvin-Helmholtz Instability
**Time needed:** 30-60 minutes  
**What you'll learn:** Fluid instabilities, shear flows, vortex formation  
**What you'll create:** Beautiful "cat's eye" vortical structures  

### Notebook 2: Sedov Blast Wave  
**Time needed:** 45-90 minutes  
**What you'll learn:** Shock waves, self-similar solutions, explosion physics  
**What you'll create:** Expanding blast waves with exact analytical comparison  

### Notebook 3: Image to Hydro
**Time needed:** 30-45 minutes  
**What you'll learn:** Creative applications, artistic physics, image processing  
**What you'll create:** Your photos evolving as fluids under gravity  

## Optional: Install SWIFT

For running actual simulations (not required for learning):

### macOS (with Homebrew)
```bash
brew install autoconf automake libtool fftw gsl hdf5
git clone https://github.com/SWIFTSIM/SWIFT
cd SWIFT
./autogen.sh
./configure --disable-mpi --disable-compiler-warnings --disable-doxygen-doc --disable-hand-vec
make
```

### Linux
```bash
# Install dependencies (Ubuntu/Debian)
sudo apt-get install autotools-dev autoconf automake libtool libfftw3-dev libgsl-dev libhdf5-dev

# Clone and build SWIFT
git clone https://github.com/SWIFTSIM/SWIFT
cd SWIFT
./autogen.sh
./configure --disable-mpi
make
```

## Troubleshooting

### "Module not found" errors
```bash
# Make sure your environment is activated
source sph-workshop-env/bin/activate
pip install -r requirements.txt
```

### SWIFT compilation issues
- Check the main README for detailed SWIFT installation instructions
- You can still use all notebooks without SWIFT installed
- The notebooks include analysis frameworks for when SWIFT becomes available

### Jupyter won't start
```bash
# Try installing/upgrading jupyter
pip install --upgrade notebook jupyter
```

## Need Help?

1. **Check the main README.md** for detailed installation instructions
2. **Look at notebook outputs** - they include example results even without simulations
3. **Try the sample data** - notebooks work with built-in examples
4. **Start with Notebook 3** if you want immediate visual results

## Quick Commands

```bash
# Generate sample images (from notebooks/ directory)
python generate_sample_images.py

# Check if SWIFT is available (from notebooks/)  
python -c "from sph_workshop_utils import check_swift_installation; check_swift_installation()"

# Create output directories
python -c "from sph_workshop_utils import create_output_directories; create_output_directories()"
```

Happy simulating! 🌌