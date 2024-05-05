import unittest
from unittest.mock import MagicMock
import numpy as np
from .fastjet_slow_version import *


class TestSlowJetAlgorithm(unittest.TestCase):
    def setUp(self):
        self.input_particles = [
            MagicMock(rapidity=lambda: 1, phi=lambda: 0, pt2=lambda: 10),
            MagicMock(rapidity=lambda: 2, phi=lambda: 1, pt2=lambda: 20),
            MagicMock(rapidity=lambda: 3, phi=lambda: 2, pt2=lambda: 30)
        ]
        self.R = 0.7

    def test_phi_mpi_pi(self):
        phi = -3 * np.pi
        adjusted_phi = phi_mpi_pi(phi)
        self.assertAlmostEqual(np.abs(adjusted_phi), np.abs(np.pi))

    def test_cluster(self):
        slow_jet_algo = SlowJetAlgorithm(self.input_particles)
        jets = slow_jet_algo.cluster(self.R)
        self.assertEqual(len(jets), 3)
        self.assertTrue(all(isinstance(jet, MagicMock) for jet in jets))


if __name__ == '__main__':
    unittest.main()
