#!/usr/bin/env python3
class Point(object):
    @staticmethod
    def distance(p1, p2):
        return abs(p1.x - p2.x) + abs(p1.y - p2.y)

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def translate(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

    @property
    def x(self): # this is the getter
        return self._x

    @x.setter
    def x(self, value): # this is the setter
        if isinstance(value, str):
            self._x = float(value)
        elif isinstance(value, float) or isinstance(value, int):
            self._x = float(value)
        else:
            raise TypeError('some useful message to be added!')

    @property
    def y(self): # this is the getter
        return self._y

    @y.setter
    def y(self, value): # this is the setter
        if isinstance(value, str):
            self._y = float(value)
        elif isinstance(value, float) or isinstance(value, int):
            self._y = float(value)
        else:
            raise TypeError('some useful message to be added!')

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return NotImplemented

    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'

class Polygon(object):
    def __init__(self, vertices):
        self._vertices = vertices[:]

    def __str__(self):
        return '<' + ', '.join(map(str, self._vertices)) + '>'

    def isadjacent(self, p1, p2):
        if p1 not in self._vertices or p2 not in self._vertices:
            return False

        index_p1 = self._vertices.index(p1)
        index_p2 = self._vertices.index(p2)
        if ((index_p1 == 0 and index_p2 == len(self._vertices) -1)
			or (index_p2 == 0 and index_p1 == len(self._vertices) -1)):
            return True

        if (abs(index_p1 - index_p2) == 1):
            return True

        return False

    ############### WRITE YOUR CODE BELOW ###########################

    def split(self, p1, p2):
        if p1 == None or p2 == None:
            raise TypeError("two inputs required")
        elif p1 == p2 or self.isadjacent(p1, p2) == True:
            raise ValueError("vertex cannot be the same of adjacent")
        elif p1 not in self._vertices or p2 not in self._vertices:
            raise ValueError("both vertices need to be within polygon")

        points1 = []
        points2 = []
        p1_index = None
        p2_index = None
        for i in range(0, len(self._vertices)):
            if self._vertices[i] == p1:
                p1_index = i
            elif self._vertices[i] == p2:
                p2_index = i

        points1 += self._vertices[0:p1_index+1]
        points2 += self._vertices[p1_index:p2_index+1]
        points1 += self._vertices[p2_index:len(self._vertices)]
        return points1, points2


vertices = [Point(0,1), Point(1,0), Point(2,0), Point(2,3), Point(0,2)]
polygon = Polygon(vertices)
print (polygon.split(Point(0,1), Point(2,0)))
p1 = Polygon([Point(0,1), Point(1,0), Point(2,0)])
p2 = Polygon([Point(0,1),Point(2,0), Point(2,3), Point(0,2)])
