#!python

from avl_tree import AVLTree
import random
import unittest

class BinaryTreeNodeTest(unittest.TestCase):

    def test_init(self):
        data = 123
        node = BinaryTreeNode(data)
        assert node.data is data
        assert node.left is None
        assert node.right is None

    def test_is_leaf(self):
        # Create node with no children
        node = BinaryTreeNode(2)
        assert node.is_leaf() is True
        # Attach left child node
        node.left = BinaryTreeNode(1)
        assert node.is_leaf() is False
        # Attach right child node
        node.right = BinaryTreeNode(3)
        assert node.is_leaf() is False
        # Detach left child node
        node.left = None
        assert node.is_leaf() is False
        # Detach right child node
        node.right = None
        assert node.is_leaf() is True

    def test_is_branch(self):
        # Create node with no children
        node = BinaryTreeNode(2)
        assert node.is_branch() is False
        # Attach left child node
        node.left = BinaryTreeNode(1)
        assert node.is_branch() is True
        # Attach right child node
        node.right = BinaryTreeNode(3)
        assert node.is_branch() is True
        # Detach left child node
        node.left = None
        assert node.is_branch() is True
        # Detach right child node
        node.right = None
        assert node.is_branch() is False

    def test_height(self):
        # Create node with no children
        node = BinaryTreeNode(4)
        assert node.height() == 0
        # Attach left child node
        node.left = BinaryTreeNode(2)
        assert node.height() == 1
        # Attach right child node
        node.right = BinaryTreeNode(6)
        assert node.height() == 1
        # Attach left-left grandchild node
        node.left.left = BinaryTreeNode(1)
        assert node.height() == 2
        # Attach right-right grandchild node
        node.right.right = BinaryTreeNode(8)
        assert node.height() == 2
        # Attach right-right-left great-grandchild node
        node.right.right.left = BinaryTreeNode(7)
        assert node.height() == 3


class TestAVLTree(unittest.TestCase):

    def test_insert_left_or_right_measure_height_rotate_maybe(self):
        numbers = [10, 5, 1]
        avlTree = AVLTree(numbers)
        

    def test_rotations(self):

    def test_rotations(self):

    def test_rotations(self):

    def test_rotations(self):

    def test_balance_factor(self):

    def test_contains(self):
    
    def test_search(self):


if __name__ == '__main__':
    unittest.main()
