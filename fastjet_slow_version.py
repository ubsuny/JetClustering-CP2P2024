import numpy as np
import fastjet as fj
import time

# Define phi_mpi_pi function to handle the periodicity of the azimuthal angle
def phi_mpi_pi(phi):
    while phi < -np.pi:
        phi += 2*np.pi
    while phi > np.pi:
        phi -= 2*np.pi
    return phi

class SlowJetAlgorithm:
    def __init__(self, particles, jet_def):
        self.particles = particles
        self.jet_def = jet_def

    def cluster(self):
        jets = []
        used_particles = set()

        for i, pi in enumerate(self.particles):
            if i not in used_particles:
                new_jet = fj.PseudoJet(pi)
                constituents = [pi]
                for j, pj in enumerate(self.particles):
                    if j not in used_particles and i != j:
                        dy = pi.rapidity() - pj.rapidity()
                        dphi = phi_mpi_pi(pi.phi() - pj.phi())
                        dR2 = dy**2 + dphi**2
                        dkt2 = min(pi.pt2(), pj.pt2()) * dR2 / (self.jet_def.R()**2)
                        if dR2 < self.jet_def.R()**2 or dkt2 < self.jet_def.R()**2:
                            new_jet += pj
                            constituents.append(pj)
                            used_particles.add(j)
                jets.append((new_jet, constituents))
                used_particles.add(i)
        
        return jets

def create_input_particles(num_particles):
    particles = []
    for _ in range(num_particles):
        px = np.random.uniform(-100.0, 100.0)
        py = np.random.uniform(-100.0, 100.0)
        pz = np.random.uniform(-10.0, 10.0)  # Use non-zero pz for full rapidity
        E = np.sqrt(px**2 + py**2 + pz**2)
        particles.append(fj.PseudoJet(px, py, pz, E))
    return particles

def main():
    num_particles = 100
    input_particles = create_input_particles(num_particles)
    R = 0.7  # Jet radius

    jet_def = fj.JetDefinition(fj.kt_algorithm, R)

    slow_jet_algo = SlowJetAlgorithm(input_particles, jet_def)

    start_time = time.time()
    slow_jets = slow_jet_algo.cluster()
    end_time = time.time()
    slow_runtime = end_time - start_time

    print("##-----------Slow Version Results-------------##")
    print("Clustered with ", jet_def.description())
    for i, (jet, constituents) in enumerate(slow_jets):
        print(f"jet {i}: pt = {jet.pt()}, y = {jet.rapidity()}, phi = {jet.phi()}")
        for j, constituent in enumerate(constituents):
            print(f"    constituent {j}'s pt: {constituent.pt()}")

    print(f"Slow clustering runtime: {slow_runtime:.6f} seconds")

    # FastJet:
    start_time = time.time()
    R = 0.7
    jet_def = fj.JetDefinition(fj.kt_algorithm, R)
    cs = fj.ClusterSequence(input_particles, jet_def)
    jets = sorted(cs.inclusive_jets(), key=lambda jet: -jet.pt())
    end_time = time.time()

    runtime = end_time - start_time
    print("##-------------fastjet Results-------------##")
    print("Clustered with", jet_def.description())
    print("        pt y phi")
    for i, jet in enumerate(jets):
        print(f"jet {i}: {jet.pt()} {jet.rapidity()} {jet.phi()}")
        constituents = jet.constituents()
        for j, constituent in enumerate(constituents):
            print(f"    constituent {j}'s pt: {constituent.pt()}")
    print(f"fastjet runtime: {runtime:.6f} seconds")


if __name__ == "__main__":
    main()
