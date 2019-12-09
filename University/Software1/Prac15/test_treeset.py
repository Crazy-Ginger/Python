import unittest
from treeset import TreeSet


class TestTreeSet(unittest.TestCase):
    def test_add_emptyset(self):
        tree = TreeSet()
        for i in [3, 1, 2, 4]:
            tree.add(i)

        # Check root
        self.assertEquals(3, tree._root)

        # check left child      
        self.assertEquals(1, tree._left._root)
        self.assertIsNone (tree._left._left)

        # check right child
        self.assertEquals(4, tree._right._root)
        self.assertIsNone (tree._right._left)
        self.assertIsNone (tree._right._right)

        # Check left->right grand child
        self.assertEquals(2, tree._left._right._root)
        self.assertIsNone (tree._left._right._left)
        self.assertIsNone (tree._left._right._right)

    def test_contains(self):
        tree = TreeSet(8)
        for i in [3,-1,6,4,7,10,14,13]:
            tree.add(i)

        for i in [3,-1,6,4,7,10,14,13]:
            self.assertTrue(i in tree)

        for i in [-2, 0, 15]:
            self.assertFalse(i in tree)
            self.assertTrue(i not in tree)

    def test_equals(self):
        treesetA = TreeSet()
        for i in [5, 19, 21, 25]:
            treesetA.add(i)

        treesetB = TreeSet()
        for i in [19, 5, 21, 25]:
            treesetB.add(i)

        treesetC = TreeSet()
        for i in [21, 19, 5, 25]:
            treesetC.add(i)

        self.assertTrue(treesetA == treesetB)
        self.assertTrue(treesetA == treesetC)
        self.assertTrue(treesetC == treesetB)
        treesetD = [19, [5, [], []], [21,[],[26,[],[]]]]
        treesetE = [19, [6, [], []], [21,[],[25,[],[]]]]
        treesetD = TreeSet()

        for i in [19, 5, 21, 26]:
            treesetD.add(i)

        treesetE = TreeSet()
        for i in [19, 6, 21, 25]:
            treesetE.add(i)

        self.assertFalse(treesetA == treesetD)
        self.assertFalse(treesetA == treesetE)
        self.assertTrue(treesetA != treesetD)
        self.assertTrue(treesetA != treesetE)

    def test_remove(self):
        treesetA = TreeSet()
        for i in [5, 19, 21, 25]:
            treesetA.add(i)

        treesetA.remove(21)
        treesetB = TreeSet()
        for i in [5, 19, 25]:
            treesetB.add(i)
        self.assertEquals(treesetA, treesetB)

        treesetA.remove(5)
        treesetA.remove(25)
        treesetC = TreeSet()
        for i in [19]:
            treesetC.add(i)
        self.assertEquals(treesetA, treesetC)

        treesetA.remove(19)
        self.assertTrue(treesetA.isempty())

    def test_union(self):
        treesetA = TreeSet()
        for i in [5, 19, 21, 25]:
            treesetA.add(i)

        treesetB = TreeSet()
        for i in [19, 6, 1, 5]:
            treesetB.add(i)

        treesetC = TreeSet()
        for i in [19, 6, 1, 5, 21, 25]:
            treesetC.add(i)

        self.assertEqual(treesetC, treesetA.union(treesetB))
        self.assertEqual(treesetA, treesetA.union(TreeSet()))





if __name__ == '__main__':
    unittest.main()

