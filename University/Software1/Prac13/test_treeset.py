#!/usr/bin/env python3
import unittest
from treeset import isempty
from treeset import add
from treeset import maxvalue
from treeset import minvalue
from treeset import get_values
from treeset import contains
from treeset import equals
from treeset import remove


class TestTreeSet(unittest.TestCase):
    def test_isempty(self):
        self.assertTrue(isempty([]))
        self.assertFalse(isempty([3,[],[]]))

    def test_add_emptyset(self):
        tree = []
        add(3, tree)
        self.assertEqual([3,[],[]], tree)
        add(3, tree)
        self.assertEqual([3,[],[]], tree)
        add(1, tree)
        self.assertEqual([3, [1, [], []], []], tree)
        add(2, tree)
        self.assertEqual([3, [1, [], [2, [], []]], []], tree)
        add(2, tree)
        self.assertEqual([3, [1, [], [2, [], []]], []], tree)
        add(4, tree)
        self.assertEqual([3, [1, [], [2, [], []]], [4, [], []]], tree)

    def test_maxvalue(self):
        treeset = []
        self.assertAlmostEqual(float('-inf'), maxvalue(treeset), delta= 0.0000001)
        treeset = [8, [3, [1,[],[]],[6,[4,[],[]],[7,[],[]]]], [10,[],[14,[13,[],
                    []],[]]]]
        self.assertAlmostEqual(14, maxvalue(treeset), delta= 0.0000001)
        self.assertAlmostEqual(0, maxvalue([0,[],[]]), delta= 0.0000001)

    def test_minvalue(self):
        treeset = []
        self.assertAlmostEqual(float('inf'), minvalue(treeset), delta= 0.0000001)
        treeset = [8, [3, [-1,[],[]],[6,[4,[],[]],[7,[],[]]]],
                    [10,[],[14,[13,[],[]],[]]]]
        self.assertAlmostEqual(-1, minvalue(treeset), delta= 0.0000001)
        self.assertAlmostEqual(0, minvalue([0,[],[]]), delta= 0.0000001)

    def test_getvalues(self):
        self.assertEqual([], get_values([]))
        self.assertEqual([3], get_values([3,[],[]]))
        treeset = [8, [3, [-1,[],[]],[6,[4,[],[]],[7,[],[]]]],
                    [10,[],[14,[13,[],[]],[]]]]
        self.assertEqual([14,13,10,8,7,6,4,3,-1], get_values(treeset))

    def test_contains(self):
        treeset = [8, [3, [-1,[],[]],[6,[4,[],[]],[7,[],[]]]],
                    [10,[],[14,[13,[],[]],[]]]]
        self.assertFalse(contains(1,[]))
        self.assertFalse(contains(1,[3,[],[]]))
        self.assertFalse(contains(0,treeset))
        self.assertFalse(contains(15,treeset))
        self.assertTrue(contains(8, treeset))
        self.assertTrue(contains(-1, treeset))
        self.assertTrue(contains(14, treeset))
        self.assertTrue(contains(13, treeset))
        self.assertTrue(contains(10, treeset))
        self.assertTrue(contains(6, treeset))

    def test_equals(self):
        treesetA = [5, [], [19, [], [21,[],[25,[],[]]]]]
        treesetB = [5, [], [21, [19, [], []], [25,[],[]]]]
        treesetC = [19, [5, [], []], [21,[],[25,[],[]]]]
        self.assertTrue(equals(treesetA, treesetB))
        self.assertTrue(equals(treesetA, treesetC))
        self.assertTrue(equals(treesetC, treesetB))
        treesetD = [19, [5, [], []], [21,[],[26,[],[]]]]
        treesetE = [19, [6, [], []], [21,[],[25,[],[]]]]
        self.assertFalse(equals(treesetA, treesetD))
        self.assertFalse(equals(treesetA, treesetE))

    def test_remove(self):
        set_a = [5,[2,[-4,[],[]], [3, [], []]],[18,[],[]]]
        remove(-4, set_a)
        self.assertEqual([5,[2,[], [3, [], []]],[18,[],[]]], set_a, 'failed to remove a leaf!')

        set_b = [5,[2,[-4,[],[]], [3, [], []]],[18,[],[21,[19,[],[]],[25,[],[]]]]]
        remove(18, set_b)
        self.assertEqual([5,[2,[-4,[],[]], [3, [], []]],[21,[19,[],[]],[25,[],[]]]], set_b, 'failed to remove node with right child only!')

        set_c = [5,[2,[-4,[],[]], [3, [], []]],[27,[21,[19,[],[]],[25,[],[]]], []]]
        remove(27, set_c)
        self.assertEqual([5,[2,[-4,[],[]], [3, [], []]],[21,[19,[],[]],[25,[],[]]]], set_c, 'failed to remove node with left child only!')

        set_d = [5,[2,[-4,[],[]], [3, [], []]],[12,[9,[],[]],[21,[19,[],[]],[25,[],[]]]]]
        remove(12, set_d)
        self.assertEqual([5,[2,[-4,[],[]], [3, [], []]],[19,[9,[],[]],[21,[],[25,[],[]]]]], set_d, 'failed to remove node two children!')


if __name__ == '__main__':
    unittest.main()
