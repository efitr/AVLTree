
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

  def insert():

  def left_rotate():

  def right_rotate():

  def search():

  def remove():