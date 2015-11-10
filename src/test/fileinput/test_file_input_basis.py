from unittest import TestCase
from src.main.fileinput import FileInputBasis
from unittest.mock import MagicMock


class TestFileInputBasis(TestCase):

    def setUp(self):
        helium = MagicMock(element='HELIUM', charge=2, mass=4, coordinates=(0.000000, 0.000000, 0.7316))
        hydrogen = MagicMock(element='HYDROGEN', charge=2, mass=1, coordiantes=(0.000000, 0.000000, -0.7316))
        nuclei_array = [helium, hydrogen]
        self.file_reader_basis = FileInputBasis('3-21G.gbs', nuclei_array)

    def test_create_basis_set_array_returns_basis_array_with_names_for_sto3g(self):
        file_reader_basis = FileInputBasis('STO-3G.gbs', self.nuclei_array)
        basis_array = file_reader_basis.create_basis_set_array()
        self.assertEquals(basis_array[0].get_name(), 'HELIUM')
        self.assertEquals(basis_array[1].get_name(), 'HYDROGEN')

    def test_create_basis_set_array_returns_basis_array_with_coordinates_for_sto3g(self):
        file_reader_basis = FileInputBasis('STO-3G.gbs', self.nuclei_array)
        basis_array = file_reader_basis.create_basis_set_array()
        self.assertEquals(basis_array[0].get_coordinates().item(0), float(0))
        self.assertEquals(basis_array[0].get_coordinates().item(1), float(0))
        self.assertEquals(basis_array[0].get_coordinates().item(2), float(0.7316))
        self.assertEquals(basis_array[1].get_coordinates().item(0), float(0))
        self.assertEquals(basis_array[1].get_coordinates().item(1), float(0))
        self.assertEquals(basis_array[1].get_coordinates().item(2), float(-0.7316))

    def test_create_basis_set_array_returns_basis_array_with_orbital_type_for_sto3g(self):
        file_reader_basis = FileInputBasis('STO-3G.gbs', self.nuclei_array)
        basis_array = file_reader_basis.create_basis_set_array()
        self.assertEquals(basis_array[0].get_primitive_gaussian_array()[0].get_orbital_type(), 'S')
        self.assertEquals(basis_array[0].get_primitive_gaussian_array()[1].get_orbital_type(), 'S')
        self.assertEquals(basis_array[0].get_primitive_gaussian_array()[2].get_orbital_type(), 'S')
        self.assertEquals(basis_array[1].get_primitive_gaussian_array()[0].get_orbital_type(), 'S')
        self.assertEquals(basis_array[1].get_primitive_gaussian_array()[1].get_orbital_type(), 'S')
        self.assertEquals(basis_array[1].get_primitive_gaussian_array()[2].get_orbital_type(), 'S')

    def test_create_basis_set_array_returns_basis_array_with_array_of_coefficients_for_sto3g(self):
        file_reader_basis = FileInputBasis('STO-3G.gbs', self.nuclei_array)
        basis_array = file_reader_basis.create_basis_set_array()
        self.assertEquals(basis_array[0].get_primitive_gaussian_array()[0].get_contraction(), 0.15432897)
        self.assertEquals(basis_array[0].get_primitive_gaussian_array()[0].get_exponent(), 6.36242139)
        self.assertEquals(basis_array[0].get_primitive_gaussian_array()[1].get_contraction(), 0.53532814)
        self.assertEquals(basis_array[0].get_primitive_gaussian_array()[1].get_exponent(), 1.15892300)
        self.assertEquals(basis_array[0].get_primitive_gaussian_array()[2].get_contraction(), 0.44463454)
        self.assertEquals(basis_array[0].get_primitive_gaussian_array()[2].get_exponent(), 0.31364979)
        self.assertEquals(basis_array[1].get_primitive_gaussian_array()[0].get_contraction(), 0.15432897)
        self.assertEquals(basis_array[1].get_primitive_gaussian_array()[0].get_exponent(), 3.42525091)
        self.assertEquals(basis_array[1].get_primitive_gaussian_array()[1].get_contraction(), 0.53532814)
        self.assertEquals(basis_array[1].get_primitive_gaussian_array()[1].get_exponent(), 0.62391373)
        self.assertEquals(basis_array[1].get_primitive_gaussian_array()[2].get_contraction(), 0.44463454)
        self.assertEquals(basis_array[1].get_primitive_gaussian_array()[2].get_exponent(), 0.16885540)

    def test_create_basis_set_array_returns_basis_array_with_correct_names_for_321g(self):
        file_reader_basis = FileInputBasis('3-21G.gbs', self.nuclei_array)
        basis_array = file_reader_basis.create_basis_set_array()
        self.assertEquals(basis_array[0].get_name(), 'HELIUM')
        self.assertEquals(basis_array[1].get_name(), 'HELIUM')
        self.assertEquals(basis_array[2].get_name(), 'HYDROGEN')
        self.assertEquals(basis_array[3].get_name(), 'HYDROGEN')

    def test_create_basis_set_array_returns_basis_array_with_correct_coordinates_for_321g(self):
        file_reader_basis = FileInputBasis('3-21G.gbs', self.nuclei_array)
        basis_array = file_reader_basis.create_basis_set_array()

        self.assertEquals(basis_array[0].get_coordinates().item(0), float(0))
        self.assertEquals(basis_array[1].get_coordinates().item(0), float(0))
        self.assertEquals(basis_array[2].get_coordinates().item(0), float(0))
        self.assertEquals(basis_array[3].get_coordinates().item(0), float(0))

        self.assertEquals(basis_array[0].get_coordinates().item(1), float(0))
        self.assertEquals(basis_array[1].get_coordinates().item(1), float(0))
        self.assertEquals(basis_array[2].get_coordinates().item(1), float(0))
        self.assertEquals(basis_array[3].get_coordinates().item(1), float(0))

        self.assertEquals(basis_array[0].get_coordinates().item(2), float(0.7316))
        self.assertEquals(basis_array[1].get_coordinates().item(2), float(0.7316))
        self.assertEquals(basis_array[2].get_coordinates().item(2), float(-0.7316))
        self.assertEquals(basis_array[3].get_coordinates().item(2), float(-0.7316))

    def test_create_basis_set_array_returns_basis_array_with_orbital_type_for_321g(self):
        file_reader_basis = FileInputBasis('3-21G.gbs', self.nuclei_array)
        basis_array = file_reader_basis.create_basis_set_array()
        self.assertEquals(basis_array[0].get_primitive_gaussian_array()[0].get_orbital_type(), 'S')
        self.assertEquals(basis_array[0].get_primitive_gaussian_array()[1].get_orbital_type(), 'S')
        self.assertEquals(basis_array[1].get_primitive_gaussian_array()[0].get_orbital_type(), 'S')
        self.assertEquals(basis_array[2].get_primitive_gaussian_array()[0].get_orbital_type(), 'S')
        self.assertEquals(basis_array[2].get_primitive_gaussian_array()[1].get_orbital_type(), 'S')
        self.assertEquals(basis_array[3].get_primitive_gaussian_array()[0].get_orbital_type(), 'S')

    def test_create_basis_set_array_returns_basis_array_with_array_of_coefficients_for_321g(self):
        file_reader_basis = FileInputBasis('3-21G.gbs', self.nuclei_array)
        basis_array = file_reader_basis.create_basis_set_array()
        self.assertEquals(basis_array[0].get_primitive_gaussian_array()[0].get_contraction(), 0.1752300)
        self.assertEquals(basis_array[0].get_primitive_gaussian_array()[0].get_exponent(), 13.6267000)
        self.assertEquals(basis_array[0].get_primitive_gaussian_array()[1].get_contraction(), 0.8934830)
        self.assertEquals(basis_array[0].get_primitive_gaussian_array()[1].get_exponent(), 1.9993500)
        self.assertEquals(basis_array[1].get_primitive_gaussian_array()[0].get_contraction(), 1.0000000)
        self.assertEquals(basis_array[1].get_primitive_gaussian_array()[0].get_exponent(), 0.3829930)
        self.assertEquals(basis_array[2].get_primitive_gaussian_array()[0].get_contraction(), 0.1562850)
        self.assertEquals(basis_array[2].get_primitive_gaussian_array()[0].get_exponent(), 5.4471780)
        self.assertEquals(basis_array[2].get_primitive_gaussian_array()[1].get_contraction(), 0.9046910)
        self.assertEquals(basis_array[2].get_primitive_gaussian_array()[1].get_exponent(), 0.8245470)
        self.assertEquals(basis_array[3].get_primitive_gaussian_array()[0].get_contraction(), 1.0000000)
        self.assertEquals(basis_array[3].get_primitive_gaussian_array()[0].get_exponent(), 0.1831920)

    def test2(self):
        basis_array = self.file_reader_basis.create_basis_set_array()
