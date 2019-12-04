#!/usr/bin/env python3

class ListNode():
    def __init__(self, data=None):
        self.data = data
        self._next = None

    def __str__(self):
        if self._next == None:
            return str(self.data) + "])"
        else:
            return str(self.data) + ", " + self._next.__str__()

class Queue():
    def __init__(self):
        self.front = None
        self.back = None

    def __str__(self):
        pass
