#!/usr/bin/env python3
import unittest
from vector import Vector

class TestVector(unittest.TestCase):
    def test_init(self):
        data = [1, 2, 3]
        v = Vector(data)
        self.assertEqual([1.0, 2.0, 3.0], v._vector)
        self.assertNotEqual(id(data), id(v._vector))

        empty = Vector()
        self.assertEqual([], empty._vector)

    def test_str(self):
        v = Vector([1, 2, 3])
        self.assertEqual('<1.0, 2.0, 3.0>', str(v))

        empty = Vector()
        self.assertEqual('<>', str(empty))

    def test_dim(self):
        v = Vector([1, 2, 3])
        self.assertEqual(3, v.dim())

        empty = Vector()
        self.assertEqual(0, empty.dim())

    def test_get(self):
        v = Vector([1, 2, 3])
        self.assertEqual(1, v.get(0))
        self.assertEqual(2, v.get(1))
        self.assertEqual(3, v.get(2))

        self.assertRaises(IndexError, v.get, 4)

    def test_set(self):
        data = [1, 2, 3]
        v = Vector(data)
        v.set(0, 4)
        v.set(1, 5)
        v.set(2, 6)
        self.assertEqual([4.0, 5.0, 6.0], v._vector)
        self.assertEqual([1, 2, 3], data)
        self.assertRaises(IndexError, v.set, 4, 7)

    def test_scalar_product(self):
        v1 = Vector([1, 2, 3])
        v2 = v1.scalar_product(3)
        self.assertEqual([1.0, 2.0, 3.0], v1._vector)
        self.assertEqual([3.0, 6.0, 9.0], v2._vector)
        v3 = Vector()
        v4 = v3.scalar_product(3)
        self.assertEqual([], v3._vector)
        self.assertEqual([], v4._vector)

    def test_add(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([0.0, 2.0, -3.0])
        v3 = v1.add(v2)
        self.assertEqual([1.0, 4.0, 0.0], v3._vector)
        self.assertNotEqual(id(v1), id(v3))
        self.assertNotEqual(id(v2), id(v3))
        self.assertNotEqual(id(v1._vector), id(v3._vector))
        self.assertNotEqual(id(v2._vector), id(v3._vector))

        self.assertRaises(TypeError, v1.add, [2.0, 3.0, 4.0])
        self.assertRaises(ValueError, v1.add, Vector([2, 2]))
        self.assertRaises(ValueError, v1.add, Vector([4, 4, 4, 4]))

    def test_equals(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([1.0, 2.0, 3.0])
        v3 = Vector([])
        v4 = Vector()
        self.assertTrue(v1.equals(v2))
        self.assertTrue(v2.equals(v1))
        self.assertTrue(v3.equals(v4))
        self.assertTrue(v4.equals(v3))
        self.assertFalse(v1.equals(Vector([1, 2])))
        self.assertFalse(v1.equals(Vector([1, 2, 3, 4])))


if __name__ == '__main__':
    unittest.main()
