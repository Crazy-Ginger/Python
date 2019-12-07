#!/usr/bin/env python3

class Vector():
    def __init__(self, data=None):
        if data != None:
            data = data.copy()
        self._vector = []
        if type(data) == list:
            for elem in data:
                self._vector.append(float(elem))

    def __str__(self):
        return "<" + str(self._vector)[1:-1] + ">"

    def dim(self):
        return len(self._vector)

    def set(self, index, value):
        self._vector[index] = float(value)

    def get(self, index):
        return self._vector[index]

    def scalar_product(self, scalar):
        temp = self._vector.copy()
        for i in range(len(temp)):
            temp[i] = temp[i]*scalar
        return Vector(temp)

    def add(self, vector):
        if type(vector) != Vector:
            raise TypeError
        if self.dim() != vector.dim():
            raise ValueError

        local_copy = self._vector.copy()
        remote_copy = vector._vector.copy()

        for i in range(len(local_copy)):
            local_copy[i] = float(local_copy[i]) + float(remote_copy[i])
        return Vector(local_copy)

    def equals(self, other_vector):
        if isinstance(other_vector, Vector) == False:
            return False
        if self.dim() != other_vector.dim():
            return False
        for i in range(self.dim()):
            if self._vector[i] != other_vector._vector[i]:
                return False
        return True
