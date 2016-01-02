from math import pi, sqrt
from math import factorial as fac


class PrimitiveBasis:

    def __init__(self, contraction, exponent, coordinates, integral_exponents):
        self.contraction = contraction
        self.exponent = exponent
        self.coordinates = coordinates
        self.integral_exponents = integral_exponents

    @property
    def normalisation(self):
        l = self.integral_exponents
        out1 = ((2 * self.exponent) / pi) ** (3 / 4)
        out2 = (8 * self.exponent) ** (l[0] + l[1] + l[2]) * fac(l[0]) * fac(l[1]) * fac(l[2])
        out3 = fac(2 * l[0]) * fac(2 * l[1]) * fac(2 * l[2])
        return out1 * sqrt(out2 / out3)
