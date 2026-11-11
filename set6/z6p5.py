from math import gcd


class Fraction:

    def __init__(self, x=0, y=1):
        if not (isinstance(x, int) and isinstance(y, int)):
            raise TypeError("Both numbers must be numbers (integers)!")
        if y == 0:
            raise ZeroDivisionError(
                "Fraction can't have zero denominator!: {}/{}".format(x, y)
            )
        self.x = x
        self.y = y

    def __str__(self):  # zwraca "x/y" lub "x" dla y=1
        return (
            "{}".format(self.x)
            if (self.x == 0 or self.y == 1)
            else "{}/{}".format(self.x, self.y)
        )

    def __repr__(self):  # zwraca "Frac(x, y)"
        return "Fraction({}, {})".format(self.x, self.y)

    def simple_frac(self):

        if self.x == 0:
            return Fraction(0, 1)
        gcd1 = gcd(self.x, self.y)
        sign1 = self.x // abs(self.x)
        sign2 = self.y // abs(self.y)
        if sign1 * sign2 == 1:
            return Fraction(abs(self.x) // gcd1, abs(self.y) // gcd1)
        else:
            return Fraction(-abs(self.x) // gcd1, abs(self.y) // gcd1)

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return (
            self.simple_frac().x == other.simple_frac().x
            and self.simple_frac().y == other.simple_frac().y
        )

    def __ne__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return not (
            self.simple_frac().x == other.simple_frac().x
            and self.simple_frac().y == other.simple_frac().y
        )

    def __lt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        # a/b < c/d jest rownowazne a*b*d**2 < c*d*b**2
        return self.x * self.y * other.y**2 < self.y**2 * other.y * other.x

    def __le__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.x * self.y * other.y**2 <= self.y**2 * other.y * other.x

    def __add__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return Fraction(self.x * other.y + self.y * other.x, self.y * other.y)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return Fraction(self.x * other.y - self.y * other.x, self.y * other.y)

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return Fraction(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        if other.x == 0:
            raise (ZeroDivisionError("You can't divide by 0!"))
        else:
            return Fraction(self.x * other.y, other.x * self.y)

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Fraction(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        if self.x == 0:
            raise (ZeroDivisionError)
        return Fraction(self.y, self.x)

    def __float__(self):
        return self.x / self.y  # float(frac)

    def __hash__(self):
        return hash(float(self))  # immutable fracs
        # w Pythonie set([2]) == set([2.0])
        # chcemy set([2]) == set([Frac(2)])


import unittest


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = Fraction(0, 1)
        self.one = Fraction(1, 1)

    def test_init(self):
        self.assertRaises(ZeroDivisionError, Fraction, 1, 0)
        self.assertRaises(TypeError, Fraction, "hello")
        self.assertEqual(self.one, Fraction(1))

    def test_str(self):
        self.assertEqual(self.zero.__str__(), "0")
        self.assertEqual(Fraction(5, 2).__str__(), "5/2")
        self.assertEqual(Fraction(3, 1).__str__(), "3")

    def test_repr(self):
        self.assertEqual(self.zero.__repr__(), "Fraction(0, 1)")
        self.assertEqual(Fraction(1, 1).__repr__(), "Fraction(1, 1)")

    def test_simple_frac(self):
        self.assertEqual(
            Fraction.simple_frac(Fraction(2, 4)).__str__(), Fraction(1, 2).__str__()
        )
        self.assertEqual(
            Fraction.simple_frac(Fraction(2, 2)).__str__(), self.one.__str__()
        )
        self.assertEqual(
            Fraction.simple_frac(Fraction(0, 2)).__str__(), self.zero.__str__()
        )

    def test_eq(self):
        self.assertTrue(self.one == self.one)
        self.assertTrue(self.one == Fraction(1, 1))
        self.assertTrue(self.one == Fraction(2, 2))

    def test_ne(self):
        self.assertFalse(self.one != self.one)
        self.assertFalse(self.one != Fraction(1, 1))
        self.assertFalse(self.one != Fraction(2, 2))

    def test_lt(self):
        self.assertTrue(self.one < Fraction(2, 1))
        self.assertTrue(self.zero < Fraction(1, 1))
        self.assertTrue(self.zero < Fraction(2, 2))

    def test_le(self):
        self.assertTrue(self.one <= Fraction(2, 1))
        self.assertTrue(self.zero <= Fraction(1, 1))
        self.assertTrue(self.zero <= Fraction(2, 2))
        self.assertTrue(self.one <= Fraction(2, 2))

    def test_add_frac(self):
        self.assertEqual(Fraction(1, 2) + Fraction(1, 3), Fraction(5, 6))
        self.assertEqual(Fraction(3, 2) + self.one, Fraction(5, 2))
        self.assertEqual(Fraction(2, 2) + self.one, Fraction(2, 1))
        self.assertEqual(Fraction(2, 2) + self.one, Fraction(4, 2))

    def test_sub_frac(self):
        self.assertEqual(Fraction(1, 2) - Fraction(1, 3), Fraction(1, 6))
        self.assertEqual(Fraction(3, 2) - self.zero, Fraction(3, 2))
        self.assertEqual(Fraction(2, 2) - self.one, self.zero)

    def test_mul_frac(self):
        self.assertEqual(Fraction(1, 2) * Fraction(1, 3), Fraction(1, 6))
        self.assertEqual(Fraction(3, 2) * self.zero, Fraction(0, 1))
        self.assertEqual(Fraction(3, 2) * self.one, Fraction(3, 2))
        self.assertEqual(Fraction(3, 3) * self.one, Fraction(1, 1))

    def test_div_frac(self):

        self.assertEqual(Fraction(1, 2) / Fraction(1, 3), Fraction(3, 2))
        self.assertEqual(Fraction(3, 2) / self.one, Fraction(3, 2))
        self.assertEqual(self.zero / self.one, self.zero)
        self.assertEqual(Fraction(3, 3) / self.one, Fraction(1, 1))
        self.assertRaises(
            ZeroDivisionError, Fraction.__truediv__, Fraction(3, 2), self.zero
        )

    def test_pos(self):  # +frac = (+1)*frac
        self.assertEqual(self.one, +self.one)
        self.assertEqual(self.one, +Fraction(2, 2))
        self.assertEqual(self.zero, +self.zero)

    def test__neg(self):  # -frac = (-1)*frac
        self.assertEqual(-self.one, Fraction(-1, 1))
        self.assertEqual(-self.one, Fraction(1, -1))
        self.assertEqual(-self.one, -Fraction(-2, -2))
        self.assertEqual(self.zero, -self.zero)

    def test_invert(self):
        self.assertEqual(self.one, ~self.one)
        self.assertEqual(Fraction(2, 1), ~Fraction(1, 2))
        self.assertRaises(ZeroDivisionError, Fraction.__invert__, self.zero)

    def test__float(self):
        self.assertEqual(self.one.__float__(), 1.0)
        self.assertEqual(Fraction(2, 1).__float__(), 2.0)
        self.assertEqual(Fraction(-2, 1).__float__(), -2.0)

    def test__hash(self):
        fr1 = Fraction(1, 2)
        fr2 = Fraction(1, 2)
        fr3 = Fraction(1, 3)
        self.assertEqual(hash(self.one), hash(Fraction(1, 1)))
        self.assertEqual(hash(self.one), hash(1))
        self.assertEqual(hash(self.one), hash(1.0))
        self.assertEqual(hash(fr1), hash(fr2))

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
