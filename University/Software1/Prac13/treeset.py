#!/usr/bin/env python3
from math import inf

# 1: adding element to tree
def add(element, tree):
    if not tree:
        tree.extend([element, [], []])
        return tree
    if element == tree[0]:
        return tree
    if tree[1] == tree[2] == []:
        if element < tree[0]:
            tree[1] = [element, [], []]
        else:
            tree[2] = [element, [], []]
        return tree

    elif element > tree[0]:
        return add(element, tree[2])
    else:
        return add(element, tree[1])

# 2: checks if the tree contains the element passed
def contains(element, treeset):
    if not treeset:
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
    if get_values(tree_a) == get_values(tree_b):
        return True
    else:
        return False

# 4:
def get_values(tree):
    if tree==[]:
        return []
    elif isinstance(tree, int):
        return [tree]
    elif len(tree) == 1:
        return tree[:1]

    elif tree[1] == tree[2] == []:
        return tree[:1]

    elif not tree[1] and tree[2]:
        return  get_values(tree[2]) + get_values(tree[0])

    elif tree[1]and not tree[2]:
        return  get_values(tree[0]) + get_values(tree[1])

    elif tree[1] and tree[2]:
        return  get_values(tree[2]) + get_values(tree[0]) +  get_values(tree[1])

# 5: checking if tree is empty
def isempty(tree):
    if tree:
        return False
    else:
        return True

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
    def __remover(element, tree):
        if tree[0] == element:
            if not tree[1] and not tree[2]:
                print ("Removing:",tree[0])
                del tree[:]

            elif tree[1] and not tree[2]:
                subtree = tree[1]
                del tree[:]
                print ("removing:",element)
                to_add = get_values(subtree)
                for elem in to_add:
                    add(elem, tree)

            elif not tree[1] and tree[2]:
                subtree = tree[2]
                del tree[:]
                print ("removing:",element)
                to_add = get_values(subtree)
                for elem in to_add:
                    add(elem, tree)

        elif element > tree[0]:
            return __remover(element, tree[2])

        elif element < tree[0]:
            return __remover(element, tree[1])

    if contains(element, tree) == False:
        return tree

    __remover(element, tree)


# extra to assist with removing elements
def get_values_h(tree):
    if tree==[]:
        return []
    elif isinstance(tree, int):
        return [tree]
    elif len(tree) == 1:
        return tree[:1]

    elif tree[1] == tree[2] == []:
        return tree[:1]

    elif not tree[1] and tree[2]:
        return  get_values_h(tree[0]) + get_values_h(tree[2])

    elif tree[1]and not tree[2]:
        return  get_values_h(tree[0]) + get_values_h(tree[1])

    elif tree[1] and tree[2]:
        return get_values_h(tree[0]) +  get_values_h(tree[1]) + get_values_h(tree[2])

# this is a better method if using a class as it doens't change the value by reference and also rebalances the tree so that it is optimal for sorting
# def remove(element, tree):
    # def __rebalance(elements, tree):
        # if elements == []:
            # # print ("passing>",elements)
            # pass
        # elif len(elements) > 1:
            # middle = round(len(elements)/2)-1
            # # print ("middle>",elements[middle])
            # # print (":middle>", elements[:middle])
            # # print ("middle:>", elements[middle+1:])
            # add(elements[middle], tree)
            # __rebalance(elements[:middle], tree)
            # __rebalance(elements[middle+1:], tree)
            # # print ()
            # return tree
        # else:
            # # print ("adding>",elements[0])
            # add(elements[0], tree)
            # # print ()
            # return tree

    # if contains(element, tree) == False:
        # return tree
    # re_tree = get_values(tree)
    # print (re_tree)
    # re_tree.remove(element)
    # print (re_tree)
    # blank = []
    # __rebalance(re_tree[::-1], blank)
    # print (blank)
    # return blank



exam = [8,[3,[1,[],[]],[6,[4,[],[]],[7,[],[]]]],[10,[],[14,[13,[],[]],[]]]]

print (get_values_h(exam))
# remove(14, exam)
# print (exam)
