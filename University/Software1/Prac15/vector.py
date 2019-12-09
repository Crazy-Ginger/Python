#!/usr/bin/env python3

class Vector():
    def __init__(self, *data):
        self._vector = []
        if not data:
            pass
        elif isinstance(data[0], list) == True:
            for elem in data[0]:
                self._vector.append(float(elem))
        else:
            for elem in data:
                self._vector.append(float(elem))

    def __str__(self):
        return "<" + str(self._vector)[1:-1] + ">"

    def dim(self):
        return len(self._vector)

    def __setitem__(self, key, value):
        self._vector[key] = float(value)

    # def set(self, index, value):
        # self._vector[index] = float(value)

    def __getitem__(self, index):
        return self._vector[index]

    # had to keep this method as testing calls it for some reason
    def get(self, index):
        return self._vector[index]

    def __mul__(self, scalar):
        return NotImplemented

    def __rmul__(self, scalar):
        temp = self._vector.copy()
        for i in range(len(temp)):
            temp[i] = temp[i]*scalar
        return Vector(temp)

    def __add__(self, vector):
        if type(vector) != Vector:
            raise TypeError
        if self.dim() != vector.dim():
            raise ValueError

        local_copy = self._vector.copy()
        remote_copy = vector._vector.copy()

        for i in range(len(local_copy)):
            local_copy[i] = float(local_copy[i]) + float(remote_copy[i])
        return Vector(local_copy)

    def __iadd__(self, vector):
        return self.__add__(vector)

    def __imul__(self, scalar):
        return self.__rmul__(scalar)


    def __eq__(self, other_vector):
        if isinstance(other_vector, Vector) == False:
            return False
        if self.dim() != other_vector.dim():
            return False
        for i in range(self.dim()):
            if self._vector[i] != other_vector._vector[i]:
                return False
        return True

    def __ne__(self, other_vector):
        if self.__eq__(other_vector) == False:
            return True
        else:
            return False
