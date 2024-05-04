# Pseudo Code: jet Clustering Algorithm

This markdown file outlines the pseudo code for creating solw version of fastjet library for jet clustering algorithm along with function and class definitions.

## the approach 
1. Define function phi_mpi_pi(phi):
    - Handle the periodicity of the azimuthal angle by adjusting phi to be in the range [-π, π]

2. Define a class SlowJetAlgorithm:
    a. Initialize with a list of particles:
        - particles: list of particles

    b. Cluster method with parameter R (jet radius):
        - jets = []  // list to store clustered jets
        - my_particles = particles  // initialize particles to be clustered

        // Cluster particles until all are clustered
        while my_particles is not empty:
            - num_particles = length(my_particles)  // number of remaining particles
            - dij = array of zeros of size num_particles x num_particles  // matrix to store distance between particles
            - diB = array of zeros of size num_particles  // array to store distance to beam for each particle

            // Calculate distance between each pair of particles and distance to beam for each particle
            for i from 0 to num_particles - 1:
                for j from 0 to num_particles - 1:
                    - dRij2[i, j] = (my_particles[i].rapidity() - my_particles[j].rapidity())^2 + phi_mpi_pi(my_particles[i].phi() - my_particles[j].phi())^2
                    - dij[i, j] = min(my_particles[i].pt2(), my_particles[j].pt2()) * (dRij2[i, j]) / (R^2)

                - diB[i] = my_particles[i].pt2()

            // Check if merging or forming new jet is required
            if length(nonzero(dij)) != 0:
                - if min(diB) < min(dij[nonzero(dij)]):
                    // Merge particles
                    - dmin = min(diB[nonzero(diB)])
                    - idx_i = index of diB where diB == dmin
                    - add my_particles[idx_i] to jets
                    - remove my_particles[idx_i] from my_particles

                - else:
                    // Form new jet
                    - dmin = min(dij[nonzero(dij)])
                    - idx_i, idx_j = indices of dij where dij == dmin
                    - combined_particle = my_particles[idx_i] + my_particles[idx_j]
                    - remove my_particles[idx_i] and my_particles[idx_j] from my_particles
                    - add combined_particle to my_particles
            else:
                // No merging possible, form new jet with the particle with minimum pt
                - dmin = min(diB[nonzero(diB)])
                - idx_i = index of diB where diB == dmin
                - add my_particles[idx_i] to jets
                - remove my_particles[idx_i] from my_particles
                - break  // exit the loop

        - return jets

3. Instantiate SlowJetAlgorithm with input_particles
4. Perform slow jet clustering with a given jet radius (R)
5. Sort the clustered jets by transverse momentum
6. Print the slow clustering results along with runtime

7. Define a function fast_jet():
    a. Start timer
    b. Define jet radius (R) and jet definition
    c. Perform fast jet clustering using a fast algorithm (e.g., fastjet library)
    d. Sort the clustered jets by transverse momentum
    e. End timer
    f. Print the fast clustering results along with runtime

8. Call fast_jet() to perform fast jet clustering
