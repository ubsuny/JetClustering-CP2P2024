#module imput
import numpy as np
import fastjet as fj
import time
import math

def create_input_particles(num_particles):
    particles = []
    for _ in range(num_particles):
        px = np.random.uniform(-100.0, 100.0)
        py = np.random.uniform(-100.0, 100.0)
        pz = np.random.uniform(-100.0, 100.0)
        E = np.sqrt(px**2 + py**2 + pz**2)
        particles.append(fj.PseudoJet(px, py, pz, E))
    return particles
R= 0.7
num_particles = 200
input_particles = create_input_particles(num_particles)
