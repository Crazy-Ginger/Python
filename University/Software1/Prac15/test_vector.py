#!/usr/bin/env python3
import unittest
from vector import Vector

class TestVector(unittest.TestCase):
    def test_init(self):
        data = [1, 2, 3]
        v = Vector(data)
        self.assertEqual([1.0, 2.0, 3.0], v._vector)
        self.assertNotEqual(id(data), id(v._vector))

        v1 = Vector(1,2,3)
        self.assertEqual([1.0, 2.0, 3.0], v1._vector)

        empty = Vector()
        self.assertEqual([], empty._vector)

    def test_get(self):
        v = Vector([1, 2, 3])
        self.assertEqual(1, v[0])
        self.assertEqual(2, v[1])
        self.assertEqual(3, v[2])
        self.assertEqual(3, v[-1])
        try:
            v[4]
        except IndexError:
            pass
        else:
            self.fail()

        self.assertRaises(IndexError, v.get, 4)

    def test_set(self):
        data = [1, 2, 3]
        v = Vector(data)
        v[0] = 4
        v[1] = 5
        v[2] = 6
        self.assertEqual([4.0, 5.0, 6.0], v._vector)
        self.assertEqual([1, 2, 3], data)
        v[-1] = 10
        self.assertEqual([4.0, 5.0, 10.0], v._vector)
        try:
            v[4] = 7
        except IndexError:
            pass
        else:
            self.fail()


    def test_scalar_product(self):
        v1 = Vector([1, 2, 3])
        v2 = 3 * v1
        self.assertEqual([1.0, 2.0, 3.0], v1._vector)
        self.assertEqual([3.0, 6.0, 9.0], v2._vector)
        v3 = Vector()
        v4 = 3 * v3
        self.assertEqual([], v3._vector)
        self.assertEqual([], v4._vector)
        try:
            v1 * 3
        except TypeError:
            pass
        else:
            self.fail()
        try:
            v1 * [2.0, 3.0, 4.0]
        except TypeError:
            pass
        else:
            self.fail()


    def test_add(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([0.0, 2.0, -3.0])
        v3 = v1 + v2
        self.assertEqual([1.0, 4.0, 0.0], v3._vector)
        self.assertNotEqual(id(v1), id(v3))
        self.assertNotEqual(id(v2), id(v3))
        self.assertNotEqual(id(v1._vector), id(v3._vector))
        self.assertNotEqual(id(v2._vector), id(v3._vector))
        try:
            v1 + [2.0, 3.0, 4.0]
        except TypeError:
            pass
        else:
            self.fail()
        try:
            v1 + Vector([2, 2])
        except ValueError:
            pass
        else:
            self.fail()
        try:
            v1 + Vector([4, 4, 4, 4])
        except ValueError:
            pass
        else:
            self.fail()

    def test_equals(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([1.0, 2.0, 3.0])
        v3 = Vector([])
        v4 = Vector()
        self.assertTrue(v1 == v2)
        self.assertTrue(v2 == v1)
        self.assertTrue(v3 == v4)
        self.assertTrue(v4 == v3)
        self.assertFalse(v1 == Vector([1, 2]))
        self.assertFalse(v1 == Vector([1, 2, 3, 4]))
        self.assertFalse(v1 == ([1, 2, 3, 4]))
        self.assertTrue(v1 != Vector([1, 2]))
        self.assertTrue(v1 != Vector([1, 2, 3, 4]))
        self.assertTrue(v1 != ([1, 2, 3, 4]))

    def test_imul(self):
        v1 = Vector([1, 2, 3])
        v1 *= 3
        self.assertEqual([3.0, 6.0, 9.0], v1._vector)
        v2 = Vector()
        v2 *= 3
        self.assertEqual([], v2._vector)
        try:
            v1 *= [2.0, 3.0, 4.0]
        except TypeError:
            pass
        else:
            self.fail()


    def test_iadd(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([0.0, 2.0, -3.0])
        v1 += v2
        self.assertEqual([1.0, 4.0, 0.0], v1._vector)
        self.assertNotEqual(id(v1), id(v2))
        self.assertNotEqual(id(v1._vector), id(v2._vector))
        try:
            v1 += [2.0, 3.0, 4.0]
        except TypeError:
            pass
        else:
            self.fail()
        try:
            v1 += Vector([2, 2])
        except ValueError:
            pass
        else:
            self.fail()
        try:
            v1 += Vector([4, 4, 4, 4])
        except ValueError:
            pass
        else:
            self.fail()


if __name__ == '__main__':
    unittest.main()
