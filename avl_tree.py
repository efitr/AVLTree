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

class Node(object):

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    self.height = 1

class AVL_tree(object):

  def __init__(self, items=None):
    self.root = None

    if items is not None:
      for item in items:
          self.insert(item)

  # Helper functions
  def get_height(self, root):
    # Purpose
    #   * Get the current height of the node you are at
    # Approach
    #   * If it is not at the root position, return 0
    #   * Return the height of the node

    if not root:
      return 0
    return root.height

  def get_balance():
    # Purpose
    #   *
    # Approach
    #   *
    
    if not root:
      return 0
    
    return self.get_height(root.left) - self.get_height(root.right)
  
  def left_rotate():
    # Note:
    #   * This is just moving pointers, focus on that
    # Purpose 
    #   * When the height from a node is two, rebalance to make it be one once more
    # Approach 1
    #   * Navigate from the node through the right pointer and from the sub node been
    #     pointed at to the left pointing pointer and make that point to the node
    #   * Make the pointer pointing to the node, now point to the sub node on the right 
    #     
    node.right.left = node
    node = node.right

    # Approach 2
    #   * Make a temporary variable that is the current node
    #   * Make the right pointer be the node
    #   * 
    #
    # NOT COMPLETE
    '''
    temp = node
    node.right = node
    node.left = temp
    '''
  
  def right_rotate():

    node.right.right = node
    node = node.left

    # BIG(O)Notation:
    # Expected Time Complexity: O(log(N))
    # Expected Space Complexity: O(log(N))
    # Current Time Complexity: ???
    # Current Space Complexity: ???

    # Purpose: 
    #   * Find whatever element 

  def find_smallest_element():
    # Just move along the node.left property recursively until the node.left is none, return that node value
    pass
  
  def find_largest_element():
    # Just move along the node.right property recursively until the node.right is none, return that node value
    pass
  
  def insert(self, key, node=None):
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
      self.root = Node(key)
      return root
    # Do I still need this line of code??
    if not node:
      return Node(key)
    # Getting the node to it's corresponding position on the 
    # binary search tree (it becomes AVL when you add the rotations)
    elif key < node.val:
      node.left = self.insert(key, node.left)
    else:
      node.right = self.insert(key, node.right)

    # Check balance factor (you are using the 
    # height of the node in the left - the one in the right )
    # 
    balance_factor = node.get_balance()

    # For rotation to happen the balance factor must 
    # be higher than one
    # There are four possible scenarios for the rotation
    if balance_factor == -2:
      # Here should rotate right
      node.right_rotate()
    elif balance factor == 2:
      # Here should rotate left
      node.left_rotate()

  def search():

  def remove():
    # BIG(O)Notation:
    # Expected Time Complexity: O(log(N))
    # Expected Space Complexity: O(log(N))
    # Current Time Complexity: ???
    # Current Space Complexity: ???
    pass