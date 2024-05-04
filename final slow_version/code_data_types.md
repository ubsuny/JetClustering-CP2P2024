# Data Types Used in the Slow Version code:

The provided code uses various data types for representing particles, performing calculations, and managing the clustering algorithm. Here's a summary of the data types used:

1. **Python Lists**[1](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
:
   - Used for storing lists of particles and jets.
   - Example: `jets = []`, `my_particles = []`

2. **NumPy Arrays** [2](https://numpy.org/doc/stable/reference/generated/numpy.array.html): 
   - Used for efficient numerical operations and array manipulation.
   - Example: `dij`, `dRij2`

3. **Custom Classes**:
   - `SlowJetAlgorithm`: Represents the slow version of the jet clustering algorithm.
     - Contains methods for clustering particles (`cluster` method).
     - Attributes include `particles`, a list of particles.
   - Example: 
     ```python
     class SlowJetAlgorithm:
         def __init__(self, particles):
             self.particles = particles
         
         def cluster(self, R):
             # Cluster particles here
             ...
     ```

4. **FastJet PseudoJet**[3](http://fastjet.fr/repo/doxygen-3.0.6/classfastjet_1_1PseudoJet.html)
:
   - Represents particles or jets in the FastJet library.
   - Contains attributes such as transverse momentum (`pt()`), rapidity (`rapidity()`), and azimuthal angle (`phi()`).
   - Example: `pi`, `pj`, `jet`

5. **Scalars**[4](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex):
   - Used for single numerical values such as radius parameters and runtime.
   - Example: `R`, `p`, `start_time`, `end_time`, `slow_runtime`, `runtime`

6. **Function Return Values**[5](https://docs.python.org/3/tutorial/controlflow.html#defining-functions):
   - Used for returning results from functions or methods.
   - Example: `jets` from the `cluster` method of `SlowJetAlgorithm`, `jets` from the `inclusive_jets` function in FastJet.

7. **Python built-in types**[6](https://docs.python.org/3/library/stdtypes.html):
   - Used for various purposes, such as integers (`int`) for indices and booleans (`bool`) for conditions.
   - Example: `i`, `j`, `idx_i`, `idx_j`, `num_particles`, `True`, `False`

8. **FastJet JetDefinition**[7](http://fastjet.fr/repo/doxygen-3.0.6/classfastjet_1_1JetDefinition.html):
   - Represents the jet definition used for clustering particles.
   - Example: `jet_def`

9. **FastJet ClusterSequence**[8](http://fastjet.fr/repo/doxygen-3.0.6/classfastjet_1_1ClusterSequence.html)
:
   - Represents the clustering sequence object used for clustering particles.
   - Example: `cs`

10. **Python `float` and `int`**[9](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex):
    - Used for floating-point and integer numeric values.
    - Example: `float`, `int`

These data types are utilized throughout the code for managing particles, clustering, and performing numerical calculations.


#References:
1. [Python List Documentation](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

2. [NumPy Array Documentation](https://numpy.org/doc/stable/reference/generated/numpy.array.html)

3. [FastJet PseudoJet Documentation](http://fastjet.fr/repo/doxygen-3.0.6/classfastjet_1_1PseudoJet.html)

4. [Python Numeric Types](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)

5. [Python Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

6. [Python Built-in Types](https://docs.python.org/3/library/stdtypes.html)

7. [FastJet JetDefinition Documentation](http://fastjet.fr/repo/doxygen-3.0.6/classfastjet_1_1JetDefinition.html)

8. [FastJet ClusterSequence Documentation](http://fastjet.fr/repo/doxygen-3.0.6/classfastjet_1_1ClusterSequence.html)

9. [Python Numeric Types](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
