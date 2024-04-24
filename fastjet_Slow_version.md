# SlowJet Algorithm for Kt-Jets with Full Rapidity
This code implements a slow jet clustering algorithm using the kt-algorithm with full rapidity. It is designed for educational purposes to understand the concepts behind jet clustering.

## Key Features:
Implements the kt-algorithm distance metric for jet clustering.
Uses full rapidity information for particles.
Provides a basic framework for understanding jet finding algorithms.

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
