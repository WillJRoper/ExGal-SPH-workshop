# ExGal-SPH-workshop

This repository contains everything you need to work through a hands-on SPH (Smoothed Particle Hydrodynamics) workshop using the SWIFT simulation code. In this workshop, you will:

- Learn the fundamentals of SPH and hydrodynamic simulations
- Generate initial conditions for classic hydrodynamic test problems
- Run and analyze the Kelvin-Helmholtz instability simulation
- Explore the Sedov blast wave and compare with analytical solutions
- Convert images to hydrodynamic simulations for creative applications
- Visualize and create movies of your simulations

This workshop is based on the [SWIFT-Workshop](https://github.com/WillJRoper/SWIFT-Workshop) but focuses specifically on SPH applications and includes additional creative exercises.

## Workshop Structure

The workshop consists of three main Jupyter notebooks:

1. **Kelvin-Helmholtz Instability** - Classic fluid instability demonstration
2. **Sedov Blast Wave** - Spherical explosion with analytical comparison
3. **Image to Hydro Simulation** - Convert any image into a fluid simulation

# Set up

Before we can start exploring SPH simulations, we need to get some software and set up an environment. This environment will ensure everything remains self-contained without messing with any of your existing Python installations. We highly recommend using a UNIX-based system (OSX/Linux), Windows users may have a harder time.

## Necessary Software

For this workshop you will need:

- *Git*, you should already have this but if not there are plenty of guides (e.g https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
- *Python*, version >3.10 preferable but not necessary but nothing lower than 3.8. If you are still using Python 2, please upgrade to a modern version.
- A suite of Python packages we will cover shortly.
- A *C compiler*, you may already have one (you can check with `which clang` on OSX, `which gcc` on Linux and `where gcc` on Windows) but if not: 
    - On OSX the default compiler is `clang`: this can be installed by running `xcode-select --install` in the terminal after installing Xcode if you don't already have it.
    - On Linux: GCC can be installed by following the guidance for your distro on installing gcc (e.g. https://www.makeuseof.com/how-to-install-c-compiler-linux/).
    - On Windows: I have little experience but it appears the accepted method is installing via MinGW-w64 (e.g. https://www.scaler.com/topics/c/c-compiler-for-windows/).
- *wget*, to download ICs (or curl on Mac). 

## Installing SWIFT

In addition to the above, to run SWIFT you will need some extra dependencies. These are listed here: https://swift.dur.ac.uk/docs/GettingStarted/compiling_code.html. All can easily be installed via package managers (on OSX I recommend using Homebrew to get them, https://brew.sh/). 

Mac Note: You may need to install the following along with libtool:
``` bash
brew install autoconf automake libtool
```

To install SWIFT run `git clone https://github.com/SWIFTSIM/SWIFT` in the terminal to get the SWIFT repo in the directory where you want it. Then enter the cloned repo and run (NOTE: see the caveats below for mac users):
``` bash
./autogen.sh
./configure --disable-mpi
make
```
If everything has run successfully you should find an executable has been created in the repo called `swift`. If it has not run smoothly (it quite probably won't have) try running `./configure --help` to see the possible options and review the output of `./configure` if any of the software listed in the dependencies hasn't been found (has `no` next to it in the table) you may need to point to it directly. Don't worry if this doesn't work flawlessly we can help get things ironed out in the workshop. If this has worked you now have an executable for running SPH simulations!

Note, if this hasn't worked you can still continue with the next steps to setup your Python environment and work through the initial condition generation parts of the notebooks.

### Pointing to dependencies

When configuring SWIFT later for actual simulations you may need to point it to the directory containing the dependency. This can be done with the `--with-xxxx` flag during configuration. For most dependencies you only need to point to the root directory of the package, for HDF5 you need to point to the executable. Here is an example pointing to `FFTW`, `GSL` and `HDF5` installed at the default location for Apple silicon Macs using Homebrew.
``` bash
./configure ... --with-fftw=/opt/homebrew/Cellar/fftw/3.3.10_1/ --with-gsl=/opt/homebrew/Cellar/gsl/2.7.1/ --with-hdf5=/opt/homebrew/Cellar/hdf5/1.14.2/bin/h5cc
```

### Mac caveats

Due to some issues with clang if you are using OSX you will need some extra configuration arguments. Instead of the above run:
``` bash
./autogen.sh
./configure --disable-mpi --disable-compiler-warnings --disable-doxygen-doc --disable-hand-vec
make
```

## Setting up the Python environment

First off let us collect together all the Python packages we will need in an environment. There are multiple ways to make a Python environment, you may have come across the `conda` method, but here we will use `venv`. Don't let this confuse you, they are both correct ways, but `venv` comes packaged with all Python distributions regardless of how you installed Python.

First, open the terminal and navigate to where you would like to create an environment. It will be stored in a directory when created, it doesn't matter where this directory is.

Next let's make the environment itself by running
``` bash
python -m venv sph-workshop-env
```
in the terminal. This command will create a blank Python environment with no packages inside a directory called `sph-workshop-env`. The name of the environment doesn't matter but it's best to keep it informative.

With the environment made we now need to activate it. This can be done by running
``` bash
source sph-workshop-env/bin/activate
```
in the terminal. You may want to make an alias for this so you don't always have to know this path but it shouldn't matter given the length of this workshop.

Now that the environment is active we need to install the packages we need. There aren't many and all can be installed via the Python package manager `pip`.

First off let's install some simple Python packages for working with arrays, making plots, and working with HDF5 format data. To install these, run the following:
``` bash
pip install numpy matplotlib h5py unyt astropy scipy pillow
```

We will also need a SWIFT helper package for interacting with the data and making initial conditions called `swiftsimio` written by Dr Josh Borrow. As before, we can install this via pip:
``` bash
pip install swiftsimio
```

Finally, we will need Jupyter Notebooks to interact with the notebooks that make up this workshop (unless you have an IDE that works with notebooks, e.g. VSCode, if so you can skip this).
``` bash
pip install notebook
```

## Cloning this repo

The vast majority of this workshop will be conducted via notebooks in this GitHub repo. You will need to clone this repo. Navigate to where you want to store the directory and run the following.
``` bash
git clone https://github.com/WillJRoper/ExGal-SPH-workshop.git
cd ExGal-SPH-workshop
```

Now we have the repo and are inside it we can start a `jupyter notebook` session and get to work (or open the repo in your IDE). To begin with notebooks, simply run
``` bash
jupyter notebook
```
on the command line and open `notebooks/01_Kelvin_Helmholtz_Instability.ipynb`.

## Workshop Content

### Notebook 1: Kelvin-Helmholtz Instability
The Kelvin-Helmholtz instability occurs when there is velocity shear between two fluid layers. This creates beautiful vortical structures and is a fundamental instability in fluid dynamics. In this notebook you will:
- Set up initial conditions with two fluid layers at different velocities
- Run a 2D SPH simulation
- Visualize the development of the instability
- Create movies showing the evolution

### Notebook 2: Sedov Blast Wave
The Sedov blast wave is the result of a strong explosion in a uniform medium. It's one of the few hydrodynamic problems with an exact analytical solution. In this notebook you will:
- Generate initial conditions with a central energy injection
- Run the simulation and compare with the analytical solution
- Explore how resolution affects the accuracy
- Visualize pressure, density, and velocity profiles

### Notebook 3: Image to Hydro Simulation
This creative exercise shows how to convert any image into initial conditions for a hydrodynamic simulation. In this notebook you will:
- Load and process an image of your choice
- Convert pixel intensities to fluid densities
- Set up the simulation with image-based initial conditions
- Watch your image evolve as a fluid under gravity and pressure forces
- Create artistic visualizations of the evolution

Have fun exploring the world of SPH!
