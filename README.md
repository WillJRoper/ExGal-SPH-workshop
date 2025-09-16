# ExGal-SPH-workshop

This repository contains everything you need to work through a hands-on SPH (Smoothed Particle Hydrodynamics) workshop using the SWIFT simulation code. In this workshop, you will:

- Learn how to run SPH simulations using SWIFT
- See the effects of different SPH schemes and parameters on Kelvin-Helmholtz instabilities
- Convert images to hydrodynamic simulations and see how they evolve (coolest videos win the prize of bragging rights!)

## Getting Started

Log in to Cosma and navigate to your working directory.

Clone this repository onto Cosma8 using the following command:

```bash
git clone https://github.com/WillJRoper/ExGal-SPH-workshop.git
cd ExGal-SPH-workshop
```

You will then find a set of set up scripts. These simplify setting up the workshop but mostly match what you have done in previous workshops.

First we want to clone SWIFT and set it up alongside our python environment (the notebooks depend on this path to SWIFT so don't rely on a version you have elsewhere).

```bash
./setup-swift.sh && ./setup-py.sh
```

Then get an interactive session on DINE2.

```bash
srun -p dine2 -A do020 -t 01:30:00 -n 1 --pty /bin/bash
```

Now we can activate our environment and start the notebook on the remote side (Cosma).

```bash
./setup-notebook.sh
```

Finaly, on your local machine, you can open an ssh tunnel and connect to the notebook using the link printed out after running `setup-notebook.sh`.

```bash
ssh -o ServerAliveInterval=60 -N -L 8888:<node>:8888 <user>@login8.cosma.dur.ac.uk
```

The first port (8888) here is the port on your local machine (which you will need to include in the URL you open in your browser). The second port (8888) is the port on the remote machine (Cosma) which was printed out by the `setup-notebook.sh` script (by default this is also 8888). The `<node>` is the compute node you were allocated by `srun` above, this is also printed out by the `setup-notebook.sh` script. Finally, `<user>` is your usual Cosma username.

Now you can get to work on either the Kelvin_Helmholtz_Instability notebook or the image_hydro notebook. The former is more "educationally enriching" while the latter is more fun. We should have time to get through both during the workshop.
