#!python

from avl_tree import AVLTree, Node
import random
import unittest

class AVLNodeTest(unittest.TestCase):

    def test_init(self):
        data = 123
        node = Node(number)
        assert node.number is number
        assert node.left is None
        assert node.right is None
        assert node.height = 1

    def test_height(self):
        # Create node with no children
        node = Node(4)
        assert node.height() == 0
        # Attach left child node
        node.left = Node(2)
        assert node.height() == 1
        # Attach right child node
        node.right = Node(6)
        assert node.height() == 1
        # Attach left-left grandchild node
        node.left.left = Node(1)
        assert node.height() == 2
        # Attach right-right grandchild node
        node.right.right = Node(8)
        assert node.height() == 2
        # Attach right-right-left great-grandchild node
        node.right.right.left = Node(7)
        assert node.height() == 3


class TestAVLTree(unittest.TestCase):

    # dictionary_for_test = {'test_insert_left_or_right_measure_rule_rotate_maybe': 'insert'}   
    def test_insert_without_rotations(self):
        numbers = [1, 2, 3]
        avlTree = AVLTree(numbers)
        assert avlTree.root.number == 1
        assert avlTree.root.left.number == 2
        assert avlTree.root.left.number == 3

        assert avlTree.root.height = 1
        assert avlTree.root.left.height = 2
        assert avlTree.root.right.height = 2

    def test_insert_with_left_left_rotation(self):
        number = [10, 5, 1]
        avlTree = AVLTree(numbers)
        assert avlTree.root.number == 5
        assert avlTree.root.left.number == 1
        assert avlTree.root.left.number == 10
        
        assert avlTree.root.height = 1
        assert avlTree.root.left.height = 2
        assert avlTree.root.right.height = 2
        
    def test_insert_with_left_right_rotation(self):
        number = [10, 1, 5]
        avlTree = AVLTree(numbers)
        assert avlTree.root.number == 5
        assert avlTree.root.left.number == 1
        assert avlTree.root.left.number == 10
        
        assert avlTree.root.height = 1
        assert avlTree.root.left.height = 2
        assert avlTree.root.right.height = 2

    def test_insert_with_left_left_rotation(self):
        number = [10, 14, 20]
        avlTree = AVLTree(numbers)
        assert avlTree.root.number == 14
        assert avlTree.root.left.number == 10
        assert avlTree.root.left.number == 20
        
        assert avlTree.root.height = 1
        assert avlTree.root.left.height = 2
        assert avlTree.root.right.height = 2

    def test_insert_with_left_left_rotation(self):
        number = [14, 20, 16]
        avlTree = AVLTree(numbers)
        assert avlTree.root.number == 16
        assert avlTree.root.left.number == 14
        assert avlTree.root.left.number == 20
        
        assert avlTree.root.height = 1
        assert avlTree.root.left.height = 2
        assert avlTree.root.right.height = 2

if __name__ == '__main__':
    unittest.main()
