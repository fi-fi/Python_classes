class Point:
    def __init__(self, x, y):
        if not isinstance(x, (int, float)):
            raise TypeError("x must be a number")
        if not isinstance(y, (int, float)):
            raise TypeError("y must be a number")
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return not self == other

    # Algebra

    def __add__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x * other.y - other.x * self.y

    def length(self):
        return (self.x**2 + self.y**2) ** (0.5)

    def __hash__(self):
        return hash((self.x, self.y))


import unittest


class TestPoint(unittest.TestCase):
    def setUp(self):
        self.myzero = Point(0, 0)
        self.myx = Point(1, 0)
        self.myy = Point(0, 1)

    def test_init(self):
        self.assertRaises(TypeError, Point, "a", 3)
        self.assertRaises(TypeError, Point, "a", [3])
        self.assertRaises(TypeError, Point, "a", "b")

    def test_str(self):
        self.assertEqual(self.myzero.__str__(), "(0, 0)")
        self.assertEqual(self.myx.__str__(), "(1, 0)")
        self.assertEqual(Point(2.85, 3.04).__str__(), "(2.85, 3.04)")

    def test_repr(self):
        self.assertEqual(self.myzero.__repr__(), "Point(0, 0)")
        self.assertEqual(self.myx.__repr__(), "Point(1, 0)")
        self.assertEqual(Point(2.85, 3.04).__repr__(), "Point(2.85, 3.04)")

    def test_neg(self):
        self.assertEqual(self.myzero, -self.myzero)
        self.assertEqual(Point(-1, 0), -self.myx)
        self.assertEqual(Point(0, -1), -self.myy)

    def test_eq(self):
        self.assertTrue(self.myzero == self.myzero)
        self.assertTrue(Point(1, 0) == self.myx)
        self.assertTrue(Point(0, -1) == -self.myy)

    def test_neq(self):
        self.assertFalse(self.myzero != self.myzero)
        self.assertFalse(Point(1, 0) != self.myx)
        self.assertFalse(Point(0, -1) != -self.myy)

    def test_add(self):
        self.assertEqual(self.myx + self.myy, Point(1, 1))
        self.assertEqual(self.myx + self.myzero, self.myx)
        self.assertEqual(self.myx + (-self.myx), self.myzero)

    def test_sub(self):
        self.assertEqual(self.myx - self.myy, Point(1, -1))
        self.assertEqual(self.myx - self.myzero, self.myx)
        self.assertTrue(self.myx - self.myx == self.myzero)

    def test_mul(self):
        self.assertEqual(self.myx * self.myy, 0)
        self.assertEqual(self.myx * self.myzero, 0)
        self.assertTrue(Point(2, 1) * Point(1, 2) == 4)

    def test_cross(self):
        self.assertEqual(self.myx.cross(self.myy), 1)
        self.assertEqual(self.myx.cross(self.myzero), 0)
        self.assertTrue(Point(2, 1).cross(Point(1, 2)) == 3)
        self.assertTrue(self.myx.cross(self.myy) == -self.myy.cross(self.myx))

    def test_length(self):
        self.assertAlmostEqual(self.myx.length(), 1)
        self.assertAlmostEqual(self.myy.length(), 1)
        self.assertAlmostEqual(self.myzero.length(), 0)
        self.assertAlmostEqual(Point(2, 1).length(), 5 ** (0.5))

    def test_hash(self):
        self.assertEqual(hash(self.myx), hash(Point(1, 0)))
        self.assertEqual(hash(self.myy), hash(Point(0, 1)))

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
