from src.main.integrals.twoelectronrepulsion import ElectronRepulsion
from src.main.integrals.twoelectronrepulsion import ObaraSaika
from src.main.integrals.twoelectronrepulsion import HeadGordonPople
from multiprocessing import Pool
import numpy as np


class TwoElectronRepulsionElement:

    def __init__(self, basis_set_array, integral, symmetry, processes):
        self.basis_set_array = basis_set_array
        self.matrix_size = len(basis_set_array)
        self.integral = integral
        self.symmetry = symmetry
        self.processes = processes

    def calculate(self, i, j, k, l):
        if self.symmetry.non_zero_integral((i, j, k, l)):
            f_mn = 0
            primitive_array_i = self.basis_set_array[i].primitive_gaussian_array
            primitive_array_j = self.basis_set_array[j].primitive_gaussian_array
            primitive_array_k = self.basis_set_array[k].primitive_gaussian_array
            primitive_array_l = self.basis_set_array[l].primitive_gaussian_array
            for primitive_a in primitive_array_i:
                for primitive_b in primitive_array_j:
                    for primitive_c in primitive_array_k:
                        for primitive_d in primitive_array_l:
                            c_1 = primitive_a.contraction
                            c_2 = primitive_b.contraction
                            c_3 = primitive_c.contraction
                            c_4 = primitive_d.contraction
                            n_1 = primitive_a.normalisation
                            n_2 = primitive_b.normalisation
                            n_3 = primitive_c.normalisation
                            n_4 = primitive_d.normalisation
                            integral = self.integral.integrate(primitive_a, primitive_b, primitive_c, primitive_d)
                            f_mn += c_1 * c_2 * c_3 * c_4 * n_1 * n_2 * n_3 * n_4 * integral
            return f_mn
        else:
            return 0.0

    def store(self):
        keys = []
        for a in range(self.matrix_size):
            for b in range(self.matrix_size):
                for c in range(self.matrix_size):
                    for d in range(self.matrix_size):
                        if not (a > b or c > d or a > c or (a == c and b > d)):
                            keys.append((a, b, c, d))

        if self.processes == 1:
            repulsion_dictionary = {}
            for index in keys:
                repulsion_dictionary[index] = self.calculate(*index)
        else:
            pool = Pool(self.processes)
            values = pool.starmap(self.calculate, keys)
            repulsion_dictionary = dict(zip(keys, values))

        repulsion_matrix = np.zeros((self.matrix_size, self.matrix_size, self.matrix_size, self.matrix_size))
        for a in range(self.matrix_size):
            for b in range(self.matrix_size):
                for c in range(self.matrix_size):
                    for d in range(self.matrix_size):
                        repulsion_matrix.itemset((a, b, c, d), repulsion_dictionary[
                        self.symmetry.sort_index(a, b, c, d)])

        return repulsion_matrix


class TwoElectronRepulsionMatrixOS(TwoElectronRepulsionElement):

    def __init__(self, basis_set_array, symmetry_matrix, processes):
        super().__init__(basis_set_array, ObaraSaika(), symmetry_matrix, processes)


class TwoElectronRepulsionMatrixCook(TwoElectronRepulsionElement):

    def __init__(self, basis_set_array, symmetry_matrix, processes):
        super().__init__(basis_set_array, ElectronRepulsion(), symmetry_matrix, processes)


class TwoElectronRepulsionMatrixHGP(TwoElectronRepulsionElement):

    def __init__(self, basis_set_array, symmetry_matrix, processes):
        super().__init__(basis_set_array, HeadGordonPople(), symmetry_matrix, processes)
