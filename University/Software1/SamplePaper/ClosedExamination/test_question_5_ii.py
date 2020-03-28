#!/usr/bin/env python3
import unittest
from question_5 import Point
from question_5 import Polygon

class TestQuestion5ii(unittest.TestCase):
    
    def test_cost(self):
        """
        Test if the method returns the right cost. You can do the calculation 
        manually, but remember to use the 1-NORM distance NOT Euclidean 
        distance.
        """
        vertices = [Point(0,0), Point(1,2), Point(2,2), Point(2,0)]
        polygon = Polygon(vertices)
        self.assertAlmostEqual(14, polygon.cost(),delta=0.0000001)

    def test_cost2(self):
        """
        Test if the method returns the right cost. You can do the calculation 
        manually, but remember to use the 1-NORM distance NOT Euclidean 
        distance.
        """
        vertices = [Point(0,1), Point(1,0), Point(2,0), Point(2,3), Point(0,2)]
        polygon = Polygon(vertices)
        self.assertAlmostEqual(24, polygon.cost(),delta=0.0000001)



if __name__ == '__main__':
    unittest.main()
