"""
SPH Workshop Helper Functions

Common utilities for the ExGal-SPH-workshop notebooks.
This module contains shared functions for initial condition generation,
analysis, and visualization across all three workshop notebooks.

Author: ExGal-SPH-workshop
"""

import os

import h5py
import matplotlib.pyplot as plt
import numpy as np


def create_output_directories():
    """
    Create the standard output directories for the workshop
    """
    directories = ["../ics", "../params", "../snapshots", "../videos"]

    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Created directory: {directory}")


def load_swift_snapshot(filename):
    """
    Load a SWIFT snapshot from HDF5 file

    Parameters:
    -----------
    filename : str
        Path to snapshot file

    Returns:
    --------
    dict : Dictionary containing particle data, or None if error
    """
    try:
        with h5py.File(filename, "r") as f:
            # Read header
            header = f["Header"]
            time = header.attrs["Time"]
            box_size = header.attrs["BoxSize"]

            # Read particle data
            part0 = f["PartType0"]

            data = {
                "time": time,
                "box_size": box_size,
                "positions": part0["Coordinates"][:],
                "velocities": part0["Velocities"][:],
                "densities": part0["Density"][:] if "Density" in part0 else None,
                "internal_energy": part0["InternalEnergy"][:],
                "smoothing_length": part0["SmoothingLength"][:]
                if "SmoothingLength" in part0
                else None,
                "masses": part0["Masses"][:],
            }

        return data
    except Exception as e:
        print(f"Error loading snapshot {filename}: {e}")
        return None


def create_movie_from_snapshots(snapshot_pattern, output_movie, framerate=10):
    """
    Create a movie from snapshot files using ffmpeg

    Parameters:
    -----------
    snapshot_pattern : str
        Pattern for snapshot files (e.g., 'snapshots/simulation_*.hdf5')
    output_movie : str
        Output movie filename
    framerate : int
        Frames per second for the movie

    Returns:
    --------
    bool : True if successful, False otherwise
    """
    try:
        # Find all snapshot files
        import glob

        snapshot_files = sorted(glob.glob(snapshot_pattern))

        if len(snapshot_files) < 2:
            print(f"Not enough snapshots found with pattern: {snapshot_pattern}")
            return False

        print(f"Found {len(snapshot_files)} snapshots")

        # Create frame directory
        frame_dir = "../videos/frames"
        os.makedirs(frame_dir, exist_ok=True)

        # Generate frames (this would need specific plotting function)
        print("Note: Frame generation requires specific plotting functions.")
        print("Use the notebook-specific movie creation functions instead.")

        return False

    except Exception as e:
        print(f"Error creating movie: {e}")
        return False


def calculate_gravitational_softening(particle_positions, softening_fraction=0.05):
    """
    Calculate appropriate gravitational softening length

    Parameters:
    -----------
    particle_positions : array
        Array of particle positions
    softening_fraction : float
        Fraction of mean inter-particle separation to use as softening

    Returns:
    --------
    float : Recommended softening length
    """
    n_particles = len(particle_positions)

    if len(particle_positions.shape) == 2:
        # 2D or 3D positions
        if particle_positions.shape[1] == 2:
            # 2D case
            area = np.ptp(particle_positions[:, 0]) * np.ptp(particle_positions[:, 1])
            typical_separation = np.sqrt(area / n_particles)
        else:
            # 3D case
            volume = (
                np.ptp(particle_positions[:, 0])
                * np.ptp(particle_positions[:, 1])
                * np.ptp(particle_positions[:, 2])
            )
            typical_separation = (volume / n_particles) ** (1 / 3)
    else:
        print("Warning: Could not determine dimensionality")
        typical_separation = 0.1

    softening = softening_fraction * typical_separation
    print(f"Recommended softening length: {softening:.4f}")

    return softening


def estimate_simulation_time(n_particles, box_size, with_gravity=True):
    """
    Rough estimate of simulation runtime

    Parameters:
    -----------
    n_particles : int
        Number of particles
    box_size : float
        Size of simulation box
    with_gravity : bool
        Whether gravity is included

    Returns:
    --------
    str : Estimated runtime description
    """

    # Very rough estimates based on typical performance
    if with_gravity:
        # Gravity scales as N log N
        complexity = n_particles * np.log(n_particles)
    else:
        # Hydro scales roughly as N
        complexity = n_particles

    # Normalize to some reference
    reference_time = 1.0  # minutes for 1000 particles, hydro only

    estimated_minutes = reference_time * (complexity / 1000)

    if estimated_minutes < 1:
        return "Less than 1 minute"
    elif estimated_minutes < 60:
        return f"Approximately {estimated_minutes:.0f} minutes"
    else:
        hours = estimated_minutes / 60
        return f"Approximately {hours:.1f} hours"


def setup_plotting_style():
    """
    Set up consistent plotting style for all notebooks
    """
    plt.style.use("default")
    plt.rcParams.update(
        {
            "figure.figsize": [12, 8],
            "font.size": 12,
            "axes.labelsize": 12,
            "axes.titlesize": 14,
            "xtick.labelsize": 11,
            "ytick.labelsize": 11,
            "legend.fontsize": 11,
            "figure.titlesize": 16,
            "lines.linewidth": 2,
            "lines.markersize": 6,
            "axes.grid": True,
            "grid.alpha": 0.3,
        }
    )


def print_workshop_info():
    """
    Print information about the workshop
    """
    print("=" * 60)
    print("         ExGal-SPH-workshop Helper Module")
    print("=" * 60)
    print("This module provides common utilities for:")
    print("  • Initial condition generation")
    print("  • SWIFT simulation management")
    print("  • Analysis and visualization")
    print("  • File I/O and data processing")
    print("")
    print("Available functions:")
    print("  • check_swift_installation()")
    print("  • create_output_directories()")
    print("  • load_swift_snapshot()")
    print("  • create_movie_from_snapshots()")
    print("  • calculate_gravitational_softening()")
    print("  • estimate_simulation_time()")
    print("  • setup_plotting_style()")
    print("=" * 60)


# Workshop constants
WORKSHOP_VERSION = "1.0.0"
WORKSHOP_AUTHOR = "ExGal-SPH-workshop"

# Physical constants (in code units)
GRAVITY_CONST = 1.0  # Gravitational constant
ADIABATIC_INDEX = 5.0 / 3.0  # For monatomic gas

# Typical scales for different problems
KELVIN_HELMHOLTZ_SCALE = {
    "box_size": [4.0, 2.0],
    "velocity_shear": 2.0,
    "density_contrast": 2.0,
}

SEDOV_SCALE = {
    "explosion_energy": 1.0,
    "background_density": 1.0,
    "explosion_radius": 0.1,
}

IMAGE_SCALE = {"box_size": 3.0, "density_contrast": 20.0, "target_particles": 3000}

if __name__ == "__main__":
    print_workshop_info()
