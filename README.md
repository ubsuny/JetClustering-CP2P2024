# JetClustering-CP2P2024

## Project Description and overview:
this project aims to perform the following:

1- implementation of slow version of Kt-Algortihm that performs Jet Clustering

2- Comparison between the clustering runtime of the slow version and the original fastjet library

## Slow Version Implementation {[more details](https://github.com/ubsuny/JetClustering-CP2P2024/blob/4ca5b77f26a2821b99c282301fa9f1d9aea162f1/final_slow_version/Slowversion.md)}

The slow version implements a simple jet clustering algorithm based on the $k_t$ algorithm. It includes a class `SlowJetAlgorithm` that clusters particles into jets using pairwise distance calculations. The clustering process involves iterating over particles and merging them based on their distances until all particles are clustered. The algorithm also handles periodicity of azimuthal angles and defines a function `phi_mpi_pi` for this purpose.

## FastJet Implementation

The FastJet implementation utilizes the FastJet library, a widely used software package for jet finding in high-energy physics. It employs the `kt_algorithm` provided by FastJet for clustering particles into jets. This implementation is expected to be significantly faster compared to the slow version due to the library's optimized algorithms.

## Project Workflow

1. **Generate Input Particles** {[input module](https://github.com/ubsuny/JetClustering-CP2P2024/blob/4fec4c4ee56dfc374b23889d9a9fb10203a362a2/final_slow_version/input_module.py)}:
   - Generate a set of random input particles with momentum values.

2. **Run Slow Version** {[code file](https://github.com/ubsuny/JetClustering-CP2P2024/blob/4fec4c4ee56dfc374b23889d9a9fb10203a362a2/final_slow_version/fastjet_slow_version.py)}:
   - Cluster particles using the slow version of the jet clustering algorithm.
   - Measure the runtime and collect the clustered jets.

3. **Run FastJet**:
   - Cluster particles using the FastJet library and the `kt_algorithm`.
   - Measure the runtime and collect the clustered jets.

4. **Compare Results** {[Results file](https://github.com/ubsuny/JetClustering-CP2P2024/blob/4fec4c4ee56dfc374b23889d9a9fb10203a362a2/final_slow_version/output_fastsjet_slowversion.txt)}:
   - Compare the runtime and accuracy of the clustered jets between the slow version and FastJet implementation.
   - Analyze any differences and draw conclusions.

## Expected Outcome

It is expected that the FastJet implementation will demonstrate significantly faster runtime compared to the slow version due to its optimized algorithms. Additionally, the accuracy of the clustered jets should be comparable between the two implementations.

## Conclusion 
This project aims to provide insights into the performance difference between a simple implementation of a jet clustering algorithm and a highly optimized library-based implementation. It highlights the importance of choosing appropriate algorithms and libraries for efficient data processing in high-energy physics experiments.
