# Particle Clustering with TensorFlow

This script demonstrates particle clustering using TensorFlow. Particle clustering is a common task in high-energy physics to identify and characterize jets of particles produced in collisions.

## Approach Overview

1. **Random Particle Generation**:
   - The script generates a random set of particles with random transverse momentum (pt), pseudo-rapidity (eta), and azimuthal angle (phi).

2. **TensorFlow Version**:
   - It performs particle clustering using TensorFlow.
   - It iteratively selects a seed particle randomly and clusters nearby particles within a radius using TensorFlow operations.
   - The clusters are stored in lists of jets along with their constituent particles.

3. **Runtime Measurement**:
   - The script measures the runtime of the TensorFlow version.

## Code Explanation

- **`generate_random_particles(num_particles)`**:
  - Generates a random set of particles with specified `num_particles`.
  - Each particle has random pt, eta, and phi values.

- **`run_jet_clustering_tf(num_particles)`**:
  - Implements particle clustering using TensorFlow.
  - Clusters particles iteratively by selecting random seeds and combining nearby particles within a radius using TensorFlow operations.
  - Returns clustered jets and their constituents.

- **`delta_r(eta1, phi1, eta2, phi2)`**:
  - Calculates the delta R distance between two particles based on their eta and phi values.

- **`print_jets_tf(jets, constituents)`**:
  - Prints the clustered jets and their constituents for the TensorFlow version.

- **Main Program**:
  - Runs the TensorFlow version for clustering.
  - Prints out the clustered jets and their constituents along with the runtime.

## Runtime Measurement

- The runtime of the TensorFlow version is measured using the `time` module.

## Usage

- Set the variable `num_particles` to control the number of particles for clustering.
- Run the script to perform particle clustering with TensorFlow and observe the results and runtime.
