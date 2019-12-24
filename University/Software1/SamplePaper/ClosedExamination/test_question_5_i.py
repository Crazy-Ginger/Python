import unittest
from question_5_modelanswers import Point
from question_5_modelanswers import Polygon

class TestQuestion5i(unittest.TestCase):
    
    def test_split(self):
        """
        Test if the method splits the polygon along a cord into two polygon given two non adjacent vertices.
        """
        vertices = [Point(0,1), Point(1,0), Point(2,0), Point(2,3), Point(0,2)]
        polygon = Polygon(vertices)
        polygons = polygon.split(Point(0,1), Point(2,0))
        p1 = Polygon([Point(0,1), Point(1,0), Point(2,0)])
        p2 = Polygon([Point(0,1),Point(2,0), Point(2,3), Point(0,2)])
        for p in polygons:
            self.assertTrue(self.equals(p, p1) or self.equals(p, p2))

    def test_adjacent_error(self):
        """
        Test if the method raises a ValueError when the two vertices are
        adjacent.
        """
        vertices = [Point(0,1), Point(1,0), Point(2,0), Point(2,3), Point(0,2)]
        polygon = Polygon(vertices)
        self.assertRaises(ValueError, polygon.split, Point(0,1), Point(0,2))

    def test_samepoint_error(self):
        """
        Test if the method raises a ValueError when the two vertices are
        adjacent.
        """
        vertices = [Point(0,1), Point(1,0), Point(2,0), Point(2,3), Point(0,2)]
        polygon = Polygon(vertices)
        self.assertRaises(ValueError, polygon.split, Point(0,2), Point(0,2))

    def test_notvertex_error(self):
        """
        Test if the method raises a ValueError when one of the point passed in 
        the parameter is not a vertex from the polygon.
        """
        vertices = [Point(0,1), Point(1,0), Point(2,0), Point(2,3), Point(0,2)]
        polygon = Polygon(vertices)
        self.assertRaises(ValueError, polygon.split, Point(2,2), Point(0,2))
        self.assertRaises(ValueError, polygon.split, Point(2,0), Point(3,3))

    def test_noneparameter_error(self):
        """
        Test if the method raises a TypeError when at least one of the 
        parameter is null.
        """
        vertices = [Point(0,1), Point(1,0), Point(2,0), Point(2,3), Point(0,2)]
        polygon = Polygon(vertices)
        self.assertRaises(TypeError, polygon.split, None, Point(0,2))
        self.assertRaises(TypeError, polygon.split, Point(2,0), None)
        self.assertRaises(TypeError, polygon.split, None, None)


 	#/////////////////////////////////////////////////////////////////////////
	#            IGNORE THE CODE BELOW, ONLY USED FOR CONVENIENCE AND
	#            SIMPLIFICATION OF THE CODE.
	#//////////////////////////////////////////////////////////////////////////

    @staticmethod
    def equals(p1,p2):
        if not isinstance(p1, Polygon) or not isinstance(p2,Polygon):
            return False
        if p1 == p2:
            return True
        if len(p1._vertices) != len(p2._vertices):
            return False
        else:
            startindex = 0
            try:
                while p1._vertices[startindex] != p2._vertices[0]:
                    startindex += 1
                currentindex = startindex
                are_equals = True

                # try clockwise
                for i in range(len(p2._vertices)):
                    if currentindex == len(p1._vertices):
                        currentindex = 0
                    if p1._vertices[currentindex] != p2._vertices[i]:
                        are_equals = False
                        break

                    currentindex += 1
                
                if are_equals:  
                    # they are equals when going thought the vertices in 
                    # clockwise order
                    return True

                # if we are here, it means that they are not equals when going 
                # through the vertices clockwise. Much check equality when 
                # going anti-clockwise
                currentindex = startindex

                # try anti-clockwise
                for i in range(len(p2._vertices)):
                    if currentindex < 0:
                        currentindex = len(p1._vertices) - 1
                    if p1._vertices[currentindex] != p2._vertices[i]:
                        return False

                    currentindex -= 1
                
                return True

            except:
                return False

if __name__ == '__main__':
    unittest.main()