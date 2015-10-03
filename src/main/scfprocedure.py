from src.main.gmatrixelements import TwoElectronPartOfTheFockMatrixElements
from src.main.densitymatrix import DensityMatrix
import numpy as np


class SCFProcedure:

    """To begin the scf procedure we will need the initial guess for the density matrix, the two electron repulsion
    integrals, the kinetic and nuclear potential energy matrix to form the H_core and the transformation matrix.
    """
    def __init__(self, two_electron_repulsions, core_hamiltonian_matrix, transformation_matrix, matrix, total_energy, nuclear_repulsion):
        self.two_electron_repulsions = two_electron_repulsions
        self.core_hamiltonian_matrix = core_hamiltonian_matrix
        self.transformation_matrix = transformation_matrix
        self.matrix = matrix
        self.total_energy = total_energy
        self.nuclear_repulsion = nuclear_repulsion
        self.previous_total_energy = 0
        self.delta_energy = 0
        self.iteration_counter = 0

    def begin_scf(self, density_matrix):

        self.iteration_counter += 1
        print('\n\n----------ITERATION: ' + str(self.iteration_counter) + str('----------'))

        print('\nDENSITY MATRIX')
        print(density_matrix)

        g_matrix_elements = TwoElectronPartOfTheFockMatrixElements(density_matrix, self.two_electron_repulsions)
        g_matrix = self.matrix.create_matrix(g_matrix_elements)
        fock_matrix = self.core_hamiltonian_matrix + g_matrix
        print('\nFOCK MATRIX')
        print(fock_matrix)

        orthonormal_fock_matrix = self.transformation_matrix.T * fock_matrix * self.transformation_matrix
        orbital_energy_matrix = np.diag(np.linalg.eig(orthonormal_fock_matrix)[0])
        print('\nORBITAL ENERGY EIGENVALUES')
        print(orbital_energy_matrix)

        orbital_coefficients_orthonormal = np.linalg.eig(orthonormal_fock_matrix)[1]
        orbital_coefficients = self.transformation_matrix * orbital_coefficients_orthonormal
        print('\nOrbital Coefficients')
        print(orbital_coefficients)

        e_total = self.total_energy.calculate_total_energy(density_matrix, self.core_hamiltonian_matrix, fock_matrix)
        print('\nTOTAL ENERGY: ' + str(e_total + self.nuclear_repulsion) + ' a.u.')

        self.delta_energy = self.previous_total_energy - e_total
        self.previous_total_energy = e_total

        """Form the density matrix for the next iteration."""
        densitymatrix = DensityMatrix(orbital_coefficients)
        density_matrix = self.matrix.create_matrix(densitymatrix)

        """Solve the for the total_energy recursively this is easier to implement but it might cause a stack overflow
        when we get into bigger basis set and bigger molecules. This is also probably inefficient."""
        if abs(self.delta_energy) > 0.0000001:
            return self.begin_scf(density_matrix)
        else:
            return e_total