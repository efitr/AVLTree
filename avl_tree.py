#############################################
##### AVL TREES
#############################################

##### Objectives:
#####  * Make the AVL data structures

##### What it is?
#####  * It is a binary tree that both of it's subtrees can't
#####  have more than one level of difference.

##### What separates it from a Binary Search Tree?
#####  * The aspects that are different are insertion and removal
#####  

class Node(object):

  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    self.height = 1

class AVL_tree(object):

  def __init__(self):
    self.root = None

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
    # Purpose 
    #   * When the height on the right side is bigger tha
    # Approach
    # * Get it to rotate to the right
    node.right
    node.left

  def right_rotate():


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
    # * Do a binary search tree
    # * Update the height of the ancestor node
    # * Get the balance factor
    # * Shape things to rotate left or right

    if self.root == None:
      self.root = Node(key)
      return root

    if not node:
      return Node(key)

    elif key < node.val:
      node.left = self.insert(key, node.left)
    else:
      node.right = self.insert(key, node.right)



    # This is meant when the value on the right 
    if root.left.get_height < root.right.get_height:

  def search():
    # BIG(O)Notation:
    # Expected Time Complexity: O(log(N))
    # Expected Space Complexity: O(log(N))

  def remove():
    # BIG(O)Notation:
    # Expected Time Complexity: O(log(N))
    # Expected Space Complexity: O(log(N))