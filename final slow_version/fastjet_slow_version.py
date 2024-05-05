from input_module import *
import time
import numpy as np


# ##-----------------------Slow version--------------------------##
# Define phi_mpi_pi function to handle the periodicity of the azimuthal angle
def phi_mpi_pi(phi):
    """
    Adjusts the azimuthal angle to lie in the range [-pi, pi].

    Args:
        phi (float): Azimuthal angle in radians.

    Returns:
        float: Adjusted azimuthal angle.
    """
    # Adjust phi to be within [-pi, pi] range
    while phi < -np.pi:
        phi += 2 * np.pi
    while phi > np.pi:
        phi -= 2 * np.pi
    return phi


class SlowJetAlgorithm:
    """
    Implements a slow version of the jet clustering algorithm.

    Attributes:
        particles (list): List of particles for clustering.
    """

    def __init__(self, particles):
        """
        Initializes the SlowJetAlgorithm with particles.

        Args:
            particles (list): List of particles for clustering.
        """
        self.particles = particles

    def cluster(self, R):
        """
        Clusters particles into jets using a slow algorithm.

        Args:
            R (float): Jet resolution parameter.

        Returns:
            list: List of clustered jets.
        """
        jets = []
        my_particles = self.particles

        # Cluster until no particles left
        while len(my_particles) != 0:
            num_particles = len(my_particles)
            dij = dRij2 = np.zeros((num_particles, num_particles))
            diB = np.zeros(num_particles)

            # Calculate pairwise distances and minimum pt
            for i, pi in enumerate(my_particles):
                for j, pj in enumerate(my_particles):
                    # Calculate distance squared between particles
                    dRij2[i, j] = (pi.rapidity() - pj.rapidity())**2 + phi_mpi_pi(pi.phi() - pj.phi())**2
                    # Calculate dij
                    dij[i, j] = min(pi.pt2(), pj.pt2()) * ((dRij2[i, j])) / (R**2)

                # Calculate diB
                diB[i] = pi.pt2()

            # If any non-zero elements in dij
            if len(np.nonzero(dij)[0]) != 0:
                # Check if minimum pt less than minimum dij
                if np.min(diB) < np.min(dij[np.nonzero(dij)]):
                    # Get index of minimum pt
                    dmin = np.min(diB[np.nonzero(diB)])
                    idx_i = np.where(diB == dmin)[0][0]
                    # Add particle to jets and remove from my_particles
                    jets.append(my_particles[idx_i])
                    my_particles.pop(idx_i)
                else:
                    # Get indices of minimum dij
                    dmin = np.min(dij[np.nonzero(dij)])
                    idx_i, idx_j = np.where(dij == dmin)[0]
                    # Combine particles and update my_particles
                    combined_particle = my_particles[idx_i] + my_particles[idx_j]
                    my_particles = list(np.delete(np.array(my_particles), (idx_i, idx_j)))
                    my_particles.append(combined_particle)
            # If all elements in dij are zero
            else:
                # Get index of minimum pt
                dmin = np.min(diB[np.nonzero(diB)])
                idx_i = np.where(diB == dmin)[0][0]
                # Add particle to jets and remove from my_particles
                jets.append(my_particles[idx_i])
                my_particles.pop(idx_i)
                break

        return jets


# Usage example
slow_jet_algo = SlowJetAlgorithm(input_particles)
start_time = time.time()
slow_jets = sorted(slow_jet_algo.cluster(R), key=lambda jet: -jet.pt())
jet_def = fj.JetDefinition(fj.kt_algorithm, R)
end_time = time.time()
slow_runtime = end_time - start_time
print("##----------------Slow Version------------------##")
print("Clustered with", jet_def.description())
for i, jet in enumerate(slow_jets):
    print(f"jet {i}: pt = {jet.pt()}, y = {jet.rapidity()}, phi = {jet.phi()}")
print(f"Slow clustering runtime: {slow_runtime:.6f} seconds")
 # ##---------------------fastjet---------------------------##


def fast_jet():
    start_time = time.time()
    R = 0.7
    # p = 1 for generalized kt algorithm
    jet_def = fj.JetDefinition(fj.kt_algorithm, R)
    cs = fj.ClusterSequence(input_particles, jet_def)
    jets = sorted(cs.inclusive_jets(), key=lambda jet: -jet.pt())
    end_time = time.time()
    runtime = end_time - start_time
    print("##-------------fastjet Results-------------##")
    print("Clustered with", jet_def.description())
    print("    pt y phi")
    if jets:
        for i, jet in enumerate(jets):
            print(f"jet {i}: {jet.pt()} {jet.rapidity()} {jet.phi()}")
            # constituents = jet.constituents()
            # for j, constituent in enumerate(constituents):
            #     print(f"  constituent {j}'s pt: {constituent.pt()}")
    print(f"fastjet runtime: {runtime:.6f} seconds")


fast_jet()
