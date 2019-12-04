#!/usr/bin/env python3
from math import inf

# 1: adding element to tree
def add(element, btree):
    def __add(element, tree):
        # if len(tree[1]) == 0 and len(tree[2]) == 0:
        if tree[1] == tree[2] == []:
            if element < tree[0]:
                tree[1] = [element, [], []]
            else:
                tree[2] = [element, [], []]
            return tree

        if element > tree[0]:
            return __add(element, tree[2])
        else:
            return __add(element, tree[1])

# 2: checks if the tree contains the element passed
def contains(element, treeset):
    if len(treeset) == 0:
        return False
    if treeset[0] == element:
        return True
    elif treeset[1] == treeset[2] == []:
        return False
    elif element > treeset[0]:
        return contains(element, treeset[2])
    elif element < treeset[0]:
        return contains(element, treeset[1])

# 3:
def equals(tree_a, tree_b):
    pass

# 4:
def get_values(tree):
    pass

# 5: checking if tree is empty
def isempty(tree):
    try:
        index = tree[0]
    except IndexError:
        return True
    else:
        return False

# 6: finding max value in tree (even if not BST)
def maxvalue(tree):
    def __maxFinder__(tree, currentMax):
        try:
            index = tree[0]
        except IndexError:
            return -inf

        if tree[0] > currentMax:
            currentMax = tree[0]

        if tree[1]:
            childMax = __maxFinder__(tree[1], currentMax)
            if childMax > currentMax:
                currentMax = childMax

        if tree[2]:
            childMax = __maxFinder__(tree[2], currentMax)
            if childMax > currentMax:
                currentMax = childMax

        return currentMax
    return __maxFinder__(tree, -inf)

# 7: finding min value in tree (even if not BST)
def minvalue(btree):
    def __minFinder__(tree, currentMin):
        try:
            index = tree[0]
        except IndexError:
            return inf

        if tree[0] < currentMin:
            currentMin = tree[0]

        if tree[1]:
            childMin = __minFinder__(tree[1], currentMin)
            if childMin < currentMin:
                currentMin = childMin

        if tree[2]:
            childMin = __minFinder__(tree[2], currentMin)
            if childMin < currentMin:
                currentMin = childMin

        return currentMin
    return __minFinder__(btree, inf)

# 8: removes the passed element from the tree
def remove(element, tree):
    pass


exam = [8,
        [3,
         [1,[],[]],
         [6,
          [4,[],[]],
          [7,[],[]]
         ]
        ],
        [10,[],
         [14,
          [13,[],[]],[]
    ]
   ]
        ]

print (add(0,exam))
