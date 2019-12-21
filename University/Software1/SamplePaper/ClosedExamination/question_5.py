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



