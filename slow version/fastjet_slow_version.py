from input_module import *

##-----------------------Slow version--------------------------##
# Define phi_mpi_pi function to handle the periodicity of the azimuthal angle
def phi_mpi_pi(phi):
    while phi < -np.pi:
        phi += 2*np.pi
    while phi > np.pi:
        phi -= 2*np.pi
    return phi

class SlowJetAlgorithm:
    def __init__(self, particles):
        self.particles = particles

    def cluster(self, R):
        jets = []
        my_particles = self.particles
        num_particles=len(my_particles)

        while(num_particles!=0):
            num_particles=len(my_particles)
            dij = dRij2 = np.zeros((num_particles,num_particles))
            diB = np.zeros(num_particles)

            for i,pi in enumerate(my_particles):
                for j,pj in enumerate(my_particles):
                    dRij2[i,j] = (pi.rapidity() - pj.rapidity())**2 + phi_mpi_pi(pi.phi() - pj.phi())**2
                    dij[i,j]  = min(pi.pt2(), pj.pt2()) * ((dRij2[i,j]))/(R**2)

                diB[i] = pi.pt2()

            if len(np.nonzero(dij)[0])!=0:
                if np.min(diB) < np.min(dij[np.nonzero(dij)]):
                    dmin = np.min(diB[np.nonzero(diB)])
                    idx_i = np.where(diB == dmin)[0][0]
                    jets.append(my_particles[idx_i])
                    my_particles.pop(idx_i)

                else:
                    dmin = np.min(dij[np.nonzero(dij)])
                    idx_i, idx_j = np.where(dij == dmin)[0]
                    combined_particle = my_particles[idx_i] + my_particles[idx_j]
                    my_particles = list(np.delete(np.array(my_particles),(idx_i,idx_j)))
                    my_particles.append(combined_particle)
            else:
                dmin = np.min(diB[np.nonzero(diB)])
                idx_i = np.where(diB == dmin)[0][0]
                jets.append(my_particles[idx_i])
                my_particles.pop(idx_i)
                break

        return jets

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
 #---------------------fastjet---------------------------#
def fast_jet():
    start_time = time.time()
    R = 0.7
    p = 1  # p = 1 for generalized kt algorithm
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
