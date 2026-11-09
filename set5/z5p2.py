from math import gcd


def improper(frac):
    if not isinstance(frac, list):
        raise TypeError("This is not a fraction!: {}".format(frac))
    if len(frac) != 2:
        raise TypeError("List is not 2- element!: {}".format(frac))
    if frac[1] == 0:
        raise ValueError("Fraction can't have zero denominator!: {}".format(frac))


def simple_frac(frac):

    improper(frac)

    if frac[0] == 0:
        return [0, 1]
    sign1 = frac[0] // abs(frac[0])
    sign2 = frac[1] // abs(frac[1])
    return (
        [
            abs(frac[0]) // gcd(frac[0], frac[1]),
            abs(frac[1]) // gcd(frac[0], frac[1]),
        ]
        if sign1 * sign2 == 1
        else [
            -abs(frac[0]) // gcd(frac[0], frac[1]),
            abs(frac[1]) // gcd(frac[0], frac[1]),
        ]
    )


def add_frac(frac1, frac2, normalize=True):

    improper(frac1)
    improper(frac2)

    result = [frac1[0] * frac2[1] + frac1[1] * frac2[0], frac1[1] * frac2[1]]

    return simple_frac(result) if normalize else result


def sub_frac(frac1, frac2, normalize=True):
    improper(frac1)
    improper(frac2)
    result = [frac1[0] * frac2[1] - frac1[1] * frac2[0], frac1[1] * frac2[1]]
    return simple_frac(result) if normalize else result


def mul_frac(frac1, frac2, normalize=True):

    improper(frac1)
    improper(frac2)

    result = [frac1[0] * frac2[0], frac1[1] * frac2[1]]

    return simple_frac(result) if normalize else result


def div_frac(frac1, frac2, normalize=True):

    improper(frac1)
    improper(frac2)

    if frac2[0] != 0:

        result = [frac1[0] * frac2[1], frac1[1] * frac2[0]]

        return simple_frac(result) if normalize else result

    else:
        raise ZeroDivisionError("You can't divide by zero!: {}".format(frac2))


def is_positive(frac):

    improper(frac)

    return frac[0] * frac[1] > 0


def is_zero(frac):

    improper(frac)

    return frac[0] == 0


def cmp_frac(frac1, frac2, Normalize=True):

    improper(frac1)
    improper(frac2)

    if simple_frac(frac1) == simple_frac(frac2):
        return 0
    return 2 * is_positive(sub_frac(frac2, frac1)) - 1


def frac2float(frac):

    improper(frac)

    return frac[0] / frac[1]


import unittest


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]
        self.one = [1, 1]

    def test_improper(self):
        self.assertEqual(improper([1, 2]), None)
        self.assertRaises(ValueError, improper, [1, 0])
        self.assertRaises(TypeError, improper, "hello")
        self.assertRaises(TypeError, improper, [1])

    def test_simple_frac(self):
        self.assertEqual(simple_frac([2, 4]), [1, 2])
        self.assertEqual(simple_frac([2, 2]), self.one)
        self.assertEqual(simple_frac([0, 2]), self.zero)

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([3, 2], self.zero), [3, 2])
        self.assertEqual(add_frac([3, 2], self.one), [5, 2])
        self.assertEqual(add_frac([2, 2], self.one), [2, 1])
        self.assertEqual(add_frac([2, 2], self.one, False), [4, 2])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(sub_frac([3, 2], self.zero), [3, 2])
        self.assertEqual(sub_frac([3, 2], self.one), [1, 2])
        self.assertEqual(sub_frac([2, 2], self.one), [0, 1])
        self.assertEqual(sub_frac([2, 2], self.one, False), [0, 2])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(mul_frac([3, 2], self.zero), [0, 1])
        self.assertEqual(mul_frac([3, 2], self.one), [3, 2])
        self.assertEqual(mul_frac([3, 3], self.one, False), [3, 3])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])
        self.assertEqual(div_frac([3, 2], self.one), [3, 2])
        self.assertEqual(div_frac(self.zero, self.one), [0, 1])
        self.assertEqual(div_frac([3, 3], self.one, False), [3, 3])
        self.assertRaises(ZeroDivisionError, div_frac, [3, 2], self.zero)

    def test_is_positive(self):
        self.assertEqual(is_positive([3, 2]), 1)
        self.assertEqual(is_positive([-3, 2]), 0)
        self.assertEqual(is_positive([3, -2]), 0)
        self.assertEqual(is_positive([-3, -2]), 1)
        self.assertEqual(is_positive([0, 1]), 0)

    def test_is_zero(self):
        self.assertEqual(is_zero(self.zero), 1)
        self.assertEqual(is_zero([0, 2]), 1)
        self.assertEqual(is_zero([1, 3]), 0)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac(self.zero, self.one), 1)
        self.assertEqual(cmp_frac(self.one, self.zero), -1)
        self.assertEqual(cmp_frac(self.zero, self.zero), 0)

    def test_frac2float(self):
        self.assertEqual(frac2float([2, 1]), 2.0)
        self.assertEqual(frac2float(self.zero), 0.0)
        self.assertEqual(frac2float([3, 2]), 3 / 2)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
