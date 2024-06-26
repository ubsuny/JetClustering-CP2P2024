# SlowJet Algorithm for Kt-Jets with Full Rapidity
This code implements a slow jet clustering algorithm using the kt-algorithm with full rapidity. It is designed for educational purposes to understand the concepts behind jet clustering.

### Full k_t-algorithm distance metric:
The distance $(d_{ij}^2)$ between two particles $(i)$ and $(j)$ is calculated as:

$d_{ij} = \min\left(p_{ti}^{p}, p_{tj}^{p}\right) \frac{\Delta_{ij}^2}{R^2}$

where:
- $p_{ti}$ and $p_{tj}$ are the transverse momenta of particles $(i)$ and $(j)$ respectively.
- $\Delta_{ij}$ is the distance between particles $(i)$ and $(j)$ in the rapidity-azimuth plane.
- $(R)$ is the radius parameter.
- $(p)$ is the power parameter. 

The distance $\Delta_{ij}$ is calculated using the following equation:

[
$\Delta_{ij}^2 = (y_i - y_j)^2 + \left(\phi_i - \phi_j\right)^2$
]

where:
- $(y_i)$ and $(y_j)$ are the rapidity values of particles $(i)$ and $(j)$ respectively.
- $\phi_i and $\phi_j are the azimuthal angles of particles $(i)$ and $(j)$ respectively.

### 

## Full rapidity:

The rapidity y is calculated as:

\[
$y = \frac{1}{2} \ln \left( \frac{E + p_z}{E - p_z} \right)$
\]

where $E$ is the energy of the particle and $p_z$ is its longitudinal momentum.

## Key Features:
Implements the kt-algorithm distance metric for jet clustering.
Uses full rapidity information for particles.
Provides a basic framework for understanding jet-finding algorithms.

## Limitations:
Slow performance: The implementation uses nested loops and explicit distance calculations, making it computationally expensive for large event sizes.
Not optimized: This code is not optimized for speed compared to libraries like FastJet.

## Components:
``` phi_mpi_pi``` function: Ensures azimuthal angles stay within -π and π for periodicity.
```SlowJetAlgorithm``` class:
Performs jet clustering using the kt-algorithm.
Takes particles and jet definition as input.
```cluster``` function iterates through particles and builds jets based on distances.
```create_input_particles``` function:
Generates random particles with momenta in all three spatial dimensions.
Calculates full energy and creates fj.PseudoJet objects.
```main``` function:
Demonstrates usage of the code for clustering and comparing runtime with FastJet (example provided).
