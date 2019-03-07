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
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    self.height = 1

class AVLTree(object):

  def __init__(self, numbers=None):
    # This is handled at the first call of the function
    # insert(value, current_node=None)
    self.root = None
    # This creates a node since the instantiation of the 
    # AVL Tree
    #self.root = Node()

    if numbers is not None:
      for number in numbers:
          self.insert_left_or_right_measure_height_(number)

  # Helper functions
  def _get_height(self, root):
    # Purpose
    #   * Get the current height of the node you are at
    # Approach
    #   * If it is not at the root position, return 0
    #   * Return the height of the node
    # How is this actually working??
    # if not root:
    #   return 0
    return root.height

  def _measure_height(self, left_node, right_node):
    # In the what part of the process this interacts that actually

    # if not root:
    #   return 0
    return self._get_height(left_node) - self._get_height(right_node)
  
  # Rotation Helper Functions
  def _left_rotate(self, node_right, node_left=None): #Maybe add the right and left node
    # Note:
    #   * This is just moving pointers, focus on that
    # Purpose 
    #   * When the height from a node is two, rebalance to make it be one once more
    # Approach 1
    #   * Navigate from the node through the right pointer and from the sub node been
    #     pointed at to the left pointing pointer and make that point to the node
    #   * Make the pointer pointing to the node, now point to the sub node on the right 
    #     
    #### If statement that depending on what conditions do what it's suppose to do
    #### there happens and double rotation
    if node_left is not None:
      
    node.right.left = node
    return node.right



  def _right_rotate(self, node):

    node.right.right = node
    node = node.left

  # Main Functions
  def insert_left_or_right_measure_height_(self, value, current_node=None):
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

    if self.root == None:
      self.root = Node(value)
      return root

    # Getting the node to it's corresponding position on the 
    # binary search tree (it becomes AVL when you add the rotations)
    elif value < node.value:
      node.left = self.insert(value, node.left)
    else:
      node.right = self.insert(value, node.right)

    # Check balance factor (you are using the 
    # height of the node in the left - the one in the right )
    # 
    current_height = node._measure_height()

    # For rotation to happen the balance factor must 
    # be higher than one
    # There are four possible scenarios for the rotation
    if current_height == -2:
      # Here should rotate right
      node.right_rotate()
    elif current_height == 2:
      # Here should rotate left
      node.left_rotate()

  def search():
    """Insert the given item in order into this binary search tree.
    TODO: Best case running time: ??? under what conditions?
    TODO: Worst case running time: ??? under what conditions?"""
    # Handle the case where the tree is empty
    if self.is_empty():
      # TODO: Create a new root node
      self.root = Node(item)
      # TODO: Increase the tree size
      self.size += 1
      return
    # Find the parent node of where the given item should be inserted
    parent = self._find_parent_node_recursive(item, self.root)
    # TODO: Check if the given item should be inserted left of parent node
    if ...:
      # TODO: Create a new node and set the parent's left child
      parent.left = ...
    # TODO: Check if the given item should be inserted right of parent node
    elif ...:
      # TODO: Create a new node and set the parent's right child
      parent.right = ...
    # TODO: Increase the tree size
    self.size +=1

  def deletion():
    # BIG(O)Notation:
    # Expected Time Complexity: O(log(N))
    # Expected Space Complexity: O(log(N))
    # Current Time Complexity: ???
    # Current Space Complexity: ???
    pass

  def find_smallest_element():
    # Just move along the node.left property recursively until the node.left is none, return that node value
    pass
  
  def find_largest_element():
    # Just move along the node.right property recursively until the node.right is none, return that node value
    pass