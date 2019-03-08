#############################################
##### AVL TREES
#############################################

##### Objectives:
#####  * Make the AVL tree data structure

##### What it is?
#####  * It is a binary tree that both of it's subtrees can't
#####  have more than one level of difference.

##### What functions are different from a Binary Search Tree?
#####  * The functions that are different are insertion and removal
#####  

# The difference between a Binary Tree and AVL Tree is that
# it balances itself, this property comes from the added 
# properties of the Node Object
#  * height serves the self balancing feature, this makes sure
#    that the height does not go further than -2 or 2 in any side
#    of the tree
class Node(object):
  def __init__(self, number):
    self.number = number
    self.left = None
    self.right = None
    self.height = 1

  def _get_height(self):
    """Return the height of this tree (the number of edges on the longest
    downward path from this tree's root node to a descendant leaf node).
    TODO: Best and worst case running time: ??? under what conditions?"""
    # TODO: Check if root node has a value and if so calculate its height

    # Check if left child has a value and if so calculate its height
    height_left_pointer_until_leaf = 0
    if self.left is not None:
        height_left_pointer_until_leaf = self.left.height() + 1
    
    # Check if right child has a value and if so calculate its height
    height_right_pointer_until_leaf = 0
    if self.right is not None:
        height_right_pointer_until_leaf = self.right.height() + 1

    return height_left_pointer_until_leaf, height_right_pointer_until_leaf

class AVLTree(object):

  def __init__(self, numbers=None):

    self.root = None

    if numbers is not None:
      for number in numbers:
          self.insert_left_or_right_measure_rule_rotate_maybe(number)

  def _measure_balance_rule(self, node):

    left_node_height, right_node_height = node._get_height()
    return left_node_height - right_node_height
  
  # Rotation Helper Functions
  def _left_rotate(self, node_right, node_left=None): #Maybe add the right and left node

    if node_left is not None:
      #Whatever is needed for the extra rotation
      node.left = node.left.right
      node.left.right.left = node.left

    node.left = node
    node = node.left.right

  def _right_rotate(self, node_left, node_right=None):
    if node_right is not None:
      node.right.left = node.right
      node.right = node.right.left.right

    node.right.left = node
    node = node.right

  # Main Functions
  def insert_left_or_right_measure_rule_rotate_maybe(self, number, current_node=None):
    # BIG(O)Notation:
    # Expected Time Complexity: O(log(N))
    # Expected Space Complexity: O(log(N))
    # Current Time Complexity: ???
    # Current Space Complexity: ???

    #Approach:
    # * Given that both sides have to be at most with one having
    #   one extra level in any side, when this breaks this has to
    #   rebalance itself rotating to the right or left
    # * Use get_height method to know that this rule is kept
    # * Use get_balance to know the current circunstances of the tree

    #Logic
    # * If there is no root, make it.
    # * Do a binary search tree
    # * Update the height of the ancestor node
    # * Get the balance factor
    # * Shape things to rotate left or right

    # This will only happen under one circunstace, it's when you have
    # not add any node at all, first number becomes the root
    if self.root == None:
      self.root = Node(number)
      return self.root

    # 
    elif number < node.number:
      node.left = self.insert_left_or_right_measure_height_rotate_maybe(number, node.left)
    else:
      node.right = self.insert_left_or_right_measure_height_rotate_maybe(number, node.right)

    # Check balance factor (you are using the 
    # height of the node in the left - the one in the right )
    # 
    current_height = self._measure_balance_rule(node)

    # For rotation to happen the balance factor must 
    # be higher than one
    # There are four possible scenarios for the rotation
    if current_height == -2:
      # Here should rotate right
      node._left_rotate()
    elif current_height == 2:
      # Here should rotate left
      node._right_rotate()

