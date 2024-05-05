# module input

'''This module generates input particles for jet clustering.
This code randomly generates px, py, pz values for the particles.'''

import numpy as np
import fastjet as fj


def create_input_particles(num_particles):
    '''Generate input particles for jet clustering.

    Args:
        num_particles (int): Number of particles to generate.

    Returns:
        list: List of PseudoJet objects representing particles.
    '''
    particles = []
    for _ in range(num_particles):
        px = np.random.uniform(-100.0, 100.0)
        py = np.random.uniform(-100.0, 100.0)
        pz = np.random.uniform(-100.0, 100.0)
        E = np.sqrt(px**2 + py**2 + pz**2)
        particles.append(fj.PseudoJet(px, py, pz, E))
    return particles


R = 0.7
num_particles = 200
input_particles = create_input_particles(num_particles)
