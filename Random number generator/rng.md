
# Random number generator using numpy
## purpose
These random number generators are used to generate random momenta for particles in the jet clustering algorithm. Each particle's momentum components (px, py, pz) are generated randomly within a specified range, and the particle's energy (E) is calculated based on these momenta.

The purpose of using random number generators is to simulate a realistic scenario where particle momenta are randomly distributed within a certain range. This ensures diverse input data for testing the jet clustering algorithm.


This Markdown document describes the random number generators used in the code and their purpose in generating input particles for the jet clustering algorithm.

## 1. `numpy.random.uniform`

The `numpy.random.uniform` function generates random numbers uniformly distributed within a specified range.

### Description:
- Generates random numbers from a uniform distribution.
- Syntax: `numpy.random.uniform(low, high, size=None)`
  - `low`: Lower boundary of the output interval.
  - `high`: Upper boundary of the output interval.
  - `size`: Shape of the output. If None, a single value is returned.

### Example Usage:
```python
px = np.random.uniform(-100.0, 100.0)
py = np.random.uniform(-100.0, 100.0)
pz = np.random.uniform(-100.0, 100.0)
