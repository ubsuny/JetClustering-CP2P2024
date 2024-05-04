# fastjet Slow version and FastJet original library Clustering runtime Comparison

## Introduction

 Jet clustering is a common technique used in high-energy physics to identify and analyze energetic particles produced in particle collisions.
 
 This document describes the implementation of a slow version of fastjet library to perform jet clustering and runtime comparison of: a slow version implemented from scratch and a fast version using the FastJet library.

 ### kt_Algorithm [1](https://arxiv.org/abs/1111.6097), [3](https://arxiv.org/pdf/0808.0792):
 The generalized \(k_t\) algorithm is a jet clustering algorithm that defines a distance measure between particles \(i\) and \(j\) as follows:
 \[
d_{ij} = \min\left(p_{ti}^{p}, p_{tj}^{p}\right) \frac{\Delta_{ij}^2}{R^2}
\]

where:
- \(p_{ti}\) and \(p_{tj}\) are the transverse momenta of particles \(i\) and \(j\) respectively.
- \(\Delta_{ij}\) is the distance between particles \(i\) and \(j\) in the rapidity-azimuth plane.
- \(R\) is the radius parameter.
- \(p\) is the power parameter. 

The distance \(\Delta_{ij}\) is calculated using the following equation:

\[
\Delta_{ij}^2 = (\y_i - \y_j)^2 + \left(\phi_i - \phi_j\right)^2
\]

where:
- \(\y_i\) and \(\y_j\) are the rapidity values of particles \(i\) and \(j\) respectively.
- \(\phi_i\) and \(\phi_j\) are the azimuthal angles of particles \(i\) and \(j\) respectively.

## Explanation

The distance \(d_{ij}\) represents the distance of particle \(i\) from particle \(j\) in the clustering process. It is computed using the minimum of the transverse momenta of the two particles raised to the power \(p\), scaled by the square of their separation and the radius parameter \(R\).

The algorithm then selects the minimum of these distances to proceed with clustering.

Additionally, the algorithm computes \(d_i^B\) as the distance of particle \(i\) from the beam, which is used to determine if a particle should be included in a jet.
 

where \( d_i^B \) is calculated as the transverse momentum squared of particle \( i \). Mathematically, it can be expressed as:

\[
d_i^B = p_{ti}^2
\]

**The clustering approach consists of the following steps, as explained in the code [1](https://arxiv.org/abs/1111.6097):**

1. **Initialize Parameters**: 
   - Set the radius parameter \( R \) for the clustering algorithm.
   - Generate a set of input particles with random momentum values.

2. **Calculate Distances**: 
   - Calculate the distances between all pairs of particles \( i \) and \( j \) using the generalized \( k_t \) algorithm formula:
     \[
     d_{ij} = \min\left(p_{ti}^{p}, p_{tj}^{p}\right) \frac{\Delta_{ij}^2}{R^2}
     \]
     where $( p_{ti}$ and $ p_{tj}$ are the transverse momenta of particles \( i \) and \( j \) respectively, \( \Delta_{ij} \) is the distance between particles \( i \) and \( j \) in the rapidity-azimuth plane, \( R \) is the radius parameter, and \( p \) is the power parameter.

3. **Calculate \( d_i^B \)**:
   - Calculate the distance of each particle \( i \) from the beam (\( d_i^B \)) as the transverse momentum squared (\( p_{ti}^2 \)).

4. **Cluster Particles**:
   - Iterate over the particles and cluster them into jets:
     - Select the pair of particles \( i \) and \( j \) with the minimum distance \( d_{ij} \).
     - If the minimum distance \( d_{ij} \) is less than the minimum \( d_i^B \), merge particles \( i \) and \( j \) into a single particle and remove them from the list of particles.
     - If the minimum distance \( d_{ij} \) is greater than or equal to the minimum \( d_i^B \), add particle \( i \) to the list of jets and remove it from the list of particles.

5. **Output**:
   - Return the clustered jets sorted by transverse momentum.

# The implementation: 

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

## Slow Version[2](https://iopscience.iop.org/article/10.1088/1742-6596/2438/1/012011/pdf), [3](https://arxiv.org/pdf/0808.0792):

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
```
 Slow clustering runtime: 5.744041 seconds
 fastjet runtime: 0.000552 seconds
 ```


 # References:
 1. [FastJet user manual](https://arxiv.org/abs/1111.6097)
 2. [An array-oriented Python interface for FastJet](https://iopscience.iop.org/article/10.1088/1742-6596/2438/1/012011/pdf)
 3. [Selected Items in Jet Algorithms](https://arxiv.org/pdf/0808.0792)