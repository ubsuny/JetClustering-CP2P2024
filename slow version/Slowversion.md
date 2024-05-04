# fastjet Slow version and FastJet original library Clustering runtime Comparison

## Introduction

 Jet clustering is a common technique used in high-energy physics to identify and analyze energetic particles produced in particle collisions.
 
 This document describes the implementation of a slow version of fastjet library to perform jet clustering and runtime comparison of: a slow version implemented from scratch and a fast version using the FastJet library.

## input module

This document describes a Python module for generating particles that will be used in jet clustering.

### Introduction

This module provides functions to create input particles that will be used to perform jet clustering.

### Functions

#### `create_input_particles(num_particles)`

This function generates random input particles for jet clustering. the generated particle will be 4-vector momenta particles.

##### Parameters
- `num_particles`: Number of particles to generate.

##### Returns
- A list of `fastjet.PseudoJet` objects representing the input particles.

#### Example Usage

```python
import numpy as np
import fastjet as fj

def create_input_particles(num_particles):
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
```

## Slow Version

The slow version of jet clustering is implemented in Python. It involves the following steps:

1. **Define `phi_mpi_pi` function:** A function to handle the periodicity of the azimuthal angle.

2. **`SlowJetAlgorithm` class:**
   - Initialize with a list of particles.
   - Cluster particles based on a given radius parameter `R`.

3. **Clustering Process:**
   - Compute distances between particles and cluster them accordingly.
   - Merge particles if necessary based on the minimum distance criteria.
   - Repeat until all particles are clustered.

4. **Output:**
   - Return clustered jets sorted by transverse momentum (pt).
   - Print information about the clustered jets and runtime.

## FastJet Version

The fast version of jet clustering uses the FastJet library, which is a C++ library with Python bindings. It involves the following steps:

1. **`fast_jet` function:**
   - Initialize with a list of particles.
   - Use the FastJet library to perform jet clustering.

2. **Clustering Process:**
   - Define jet definition using FastJet.
   - Perform clustering using the defined algorithm and parameters.

3. **Output:**
   - Return clustered jets sorted by transverse momentum (pt).
   - Print information about the clustered jets and runtime.

## Usage

To use these implementations, follow these steps:

1. Provide a list of particles as input using the '''input_module.py```.
2. Choose a radius parameter `R` for clustering.

### Example

```python
import input

# Instantiate SlowJetAlgorithm with particles
slow_jet_algo = SlowJetAlgorithm(input_particles)

# Cluster using slow algorithm
slow_jets = sorted(slow_jet_algo.cluster(R), key=lambda jet: -jet.pt())

# Print slow clustering results
print("##----------------Slow Version------------------##")
print("Clustered with", jet_def.description())
for i, jet in enumerate(slow_jets):
    print(f"jet {i}: pt = {jet.pt()}, y = {jet.rapidity()}, phi = {jet.phi()}")
```

# Runtime Comparison:

runtime was calculated for both jet clustering methods and it appeared that the slow version took much longer to perform the clustering while fastjet library took much more smaller time due to optimizated built in function that allow very fast processing. 
 