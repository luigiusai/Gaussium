from math import factorial as fac


class Binomial:

    @staticmethod
    def combination(n, k):
        if k <= n:
            ans = fac(n) / (fac(k) * fac(n - k))
            return ans
        else:
            return 0

    @classmethod
    def coefficient(cls, j, l_1, l_2, a, b):
        ans = 0
        for k in range(max(0, j - l_2), min(j, l_1) + 1):
            ans += cls.combination(l_1, k) * cls.combination(l_2, j - k) * a**(l_1 - k) * b**(l_2 + k - j)
        return ans
