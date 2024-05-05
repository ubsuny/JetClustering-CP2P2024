import time
import random
import numpy as np
import tensorflow as tf

def generate_random_particles(num_particles):
    """
    Generate random particles with random transverse momentum, pseudorapidity, and azimuthal angle.

    Args:
        num_particles (int): Number of particles to generate.

    Returns:
        numpy.ndarray: Array of shape (num_particles, 3) containing pt, eta, and phi of particles.
    """
    pt = np.random.uniform(low=0, high=100, size=num_particles)
    eta = np.random.uniform(low=-1, high=1, size=num_particles)
    phi = np.random.uniform(low=0, high=2 * np.pi, size=num_particles)
    particles = np.stack([pt, eta, phi], axis=1)
    return particles

def run_jet_clustering_tf(num_particles):
    """
    Cluster particles using TensorFlow.

    Args:
        num_particles (int): Number of particles to cluster.

    Returns:
        tuple: Tuple containing list of jets and list of constituent particles for each jet.
    """
    # Generate random particles
    particles = generate_random_particles(num_particles)

    # Initialize lists to store jets and their constituents
    jets = []
    constituents = []

    # Loop over particles
    while particles.shape[0] > 0:
        # Select a seed particle randomly
        seed_index = random.randint(0, particles.shape[0] - 1)
        seed = particles[seed_index]

        # Identify nearby particles
        distances = delta_r(seed[1], seed[2], particles[:, 1], particles[:, 2])
        nearby_indices = tf.where(distances < 0.7)[:, 0]

        # Combine nearby particles into a cluster
        cluster = tf.reduce_sum(tf.gather(particles, nearby_indices), axis=0)
        jets.append(cluster.numpy())

        # Save constituents of the cluster
        constituents.append(particles[nearby_indices.numpy()])

        # Remove clustered particles
        particles = np.delete(particles, nearby_indices.numpy(), axis=0)

    return jets, constituents

def delta_r(eta1, phi1, eta2, phi2):
    """
    Calculate deltaR between two sets of pseudorapidities and azimuthal angles.

    Args:
        eta1 (float): Pseudorapidity of the first set of particles.
        phi1 (float): Azimuthal angle of the first set of particles.
        eta2 (float): Pseudorapidity of the second set of particles.
        phi2 (float): Azimuthal angle of the second set of particles.

    Returns:
        float: DeltaR between the two sets of particles.
    """
    deta = eta1 - eta2
    dphi = np.abs(phi1 - phi2)
    dphi = np.minimum(dphi, 2 * np.pi - dphi)
    return np.sqrt(deta**2 + dphi**2)

def print_jets_tf(jets, constituents):
    """
    Print out the information of clustered jets and their constituents.

    Args:
        jets (list): List of jets, each represented by [pt, y, phi].
        constituents (list): List of constituent particles for each jet.
    """
    print("        pt y phi")
    for i, jet in enumerate(jets):
        pt = jet[0]
        y = jet[1]
        phi = jet[2]
        print(f"jet {i}: {pt} {y} {phi}")
        for j, constituent in enumerate(constituents[i]):
            print(f"    constituent {j}'s pt: {constituent[0]}")

num_particles = 10  # Set the number of particles

# TensorFlow Version
start_time = time.time()
tf_jets, tf_constituents = run_jet_clustering_tf(num_particles)
end_time_tf = time.time()

# Print out results and comparison
print("TensorFlow Version - Clustered")
print_jets_tf(tf_jets, tf_constituents)
print("TensorFlow Runtime:", end_time_tf - start_time, "seconds")
