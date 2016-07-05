from unittest import TestCase
from unittest.mock import MagicMock
from numpy import testing
from src.main.objects import MoleculeFactory


class TestSymmetryHe(TestCase):

    def setUp(self):
        helium_1 = MagicMock(element='HELIUM', charge=2, mass=4, coordinates=(-0.98781, 0.41551, 0.00000))
        self.nuclei_array_he = [helium_1]
        self.molecule_factory = MoleculeFactory()

    def test_move_nuclei_to_the_origin(self):
        helium = self.molecule_factory .point_group(self.nuclei_array_he).nuclei_array[0]
        testing.assert_array_equal(helium.coordinates, (0.0, 0.0, 0.0))

    def test_point_group_returns_c_1_symmetry_for_helium(self):
        symmetry = self.molecule_factory.point_group(self.nuclei_array_he).point_group.label
        testing.assert_equal(symmetry, 'C_{1}')