
#############################################
##### AVL TREES
#############################################

##### Objectives:
#####  * Make the AVL data structures

##### What it is?
#####  * It is a binary tree that both of it's subtrees can't
#####  have more than one level of difference.

class Node(object):

  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    self.height = 1

class AVL_tree(object):

  def get_height(self, root):
    if not root:
      return 0
    return root.height

  def get_balance():
    if not root:
      return 0
    
    return self.get_height(root.left) - self.get_height(root.right)

  def insert(self, root, key):

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

    if not root:
      return Node(key)
    elif key < root.val:
      root.left = self.insert(root.left, key)
    else:
      root.right = self.insert(root.right, key)

  def left_rotate():
    # Approach
    # * Get it to rotate to the right

  def right_rotate():

  def search():

  def remove():