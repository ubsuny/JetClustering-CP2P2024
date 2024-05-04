# Jet Clustering
## What Are Jets? [1](https://cms.cern/news/jets-cms-and-determination-their-energy-scale)
"jets" refer to collimated hadrons produced during strong high-energy particle interactions, particularly in experiments conducted at particle accelerators. 
The partons (eg. produced quarks and gluons) hadronize creating hadrons which are collimated together creating the ”Jets”

##What is Jet Clustering?
 Jet clustering is a computational process used in particle physics to identify and analyze jets.
<img width="471" alt="image" src="https://github.com/ubsuny/JetClustering-CP2P2024/assets/38404107/48d7b95e-a251-4bd0-bfbd-077baad1716d">

Fig.(1)[Jets are the experimental signatures of quarks and gluons produced in high-energy processes such as head-on proton-proton collisions](https://github.com/ubsuny/JetClustering-CP2P2024/assets/38404107/8cf340c3-6493-4ee5-a527-a5af587ca0d2)
][1](https://cms.cern/news/jets-cms-and-determination-their-energy-scale)

## Why Jet Clustering?
 Individual hadrons within a jet can not to be directly resolved by detectors.
Grouping Particles:  reconstruct these jets by grouping the final state particles based on their properties, typically their momenta (energies and directions).
Further analysis can be done on the reconstructed jets.

<img width="414" alt="image" src="https://github.com/ubsuny/JetClustering-CP2P2024/assets/38404107/99bbd06f-edb4-49c8-88cd-0d57a1c84892">

Fig.(2)[3][Double Higgs production at CMS](https://www.researchgate.net/publication/362844439_Double_Higgs_production_at_CMS)

## Jet clustering algorithms
Sequential Recombination Algorithms: 
It starts with the final state particles, merges the closest pair of jets into a pseudo-jet until a certain condition is met (e.g. Energy threshold, max no. of jets). Example: Kt- Algorithm, Anti-kt Algorithm, ..etc.
K-means Algorithm: Less common in jet clustering, but can be used in specific cases.

##Fastjet:
it is a C++ library used for jet finding in high-energy physics analyses.
It provides efficient and robust algorithms for jet clustering.
It has a python version 

## Popular Jet clustering algorithms:
### Kt-Algorithm: 
#### Overview

The `kt_algorithm` is a sequential clustering algorithm used for jet finding. It works by clustering particles based on their pairwise distances and merging the closest particles iteratively until all particles are clustered into jets.

#### Parameters

The `kt_algorithm` takes one parameter:
- **Radius $(R)$**: The radius parameter $(R)$ defines the distance scale for clustering. Particles within a distance $(R)$ are considered close enough to be merged into a jet.

#### Algorithm

The `kt_algorithm` works as follows:

1. **Initialization**:
   - Start with all particles as individual jets.

2. **Clustering**:
   - Compute the pairwise distances between all particles.
   - Merge the closest pair of particles into a single jet.
   - Repeat the process until all particles are clustered into jets.

3. **Termination**:
   - Stop when no pairs of particles are within a distance \( R \) of each other.

#### Mathematical Formulation

The distance $d_{ij}$ between particles $(i)$ and $(j)$ in the $k_t$ algorithm is defined as:

\[
$d_{ij} = \min\left(p_{ti}^2, p_{tj}^2\right) \frac{\Delta_{ij}^2}{R^2}$
\]

where:
- $p_{ti}$ and $p_{tj}$ are the transverse momenta of particles $(i)$ and $(j)$ respectively.
- $\Delta_{ij}$ is the distance between particles $(i)$ and $(j)$ in the rapidity-azimuth plane.
- $(R)$ is the radius parameter.

#### Usage

To use the `kt_algorithm` in FastJet, follow these steps in your Python code:

```python
import fastjet as fj

# Define radius parameter
R = 0.7

# Define jet definition using kt_algorithm
jet_def = fj.JetDefinition(fj.kt_algorithm, R)

# Perform clustering using ClusterSequence
cs = fj.ClusterSequence(input_particles, jet_def)
jets = cs.inclusive_jets()
```




References:

1- [JETS AT CMS AND THE DETERMINATION OF THEIR ENERGY SCALE](https://cms.cern/news/jets-cms-and-determination-their-energy-scale)

2- [anti-kt algorithm](https://arxiv.org/abs/0802.1189)

3- [Double Higgs production at CMS](https://www.researchgate.net/publication/362844439_Double_Higgs_production_at_CMS)
