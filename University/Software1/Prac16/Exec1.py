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

class Stack():
    def __init__(self):
        self._top = None

    def __str__(self):
        return "LinkedStack([" + str(self._top.__str__())

    def __len__(self):
        inc = 0
        index = self._top
        while index._next != None:
            index = index._next
            inc += 1
        return inc+1

    def push(self, value):
        new = ListNode()
        new._next = self._top
        new.data = value
        self._top = new

    def pop(self):
        if self._top == None:
            raise ValueError ("Empty stack")
        popped = self._top.data
        self._top = self._top._next
        return popped

    def peek(self):
        if self._top == None:
            raise ValueError ("Empty stack")
        return self._top.data

