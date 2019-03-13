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

    # Is this actually working?, 

    # Check if left child has a value and if so calculate its height
    height_left_pointer_until_leaf = 0
    if self.left is not None:
      height_left_pointer_until_leaf = self.left.height + 1
    
    # Check if right child has a value and if so calculate its height
    height_right_pointer_until_leaf = 0
    if self.right is not None:
      height_right_pointer_until_leaf = self.right.height + 1

    return height_left_pointer_until_leaf, height_right_pointer_until_leaf

class AVLTree(object):

  def __init__(self, numbers=None):

    self.root = None

    if numbers is not None:
      for number in numbers:
          self.insert(number)

  # Do I actually need this, maybe just not make this call height, it can just make things more
  # syntactically explanation
  def _measure_balance_rule(self, node):
    # The get height shouldnt happen
    left_node_height, right_node_height = node._get_height()
    return left_node_height - right_node_height
  
  # Rotation Helper Functions
  def _left_rotate(self, node, left_side_=False): #Maybe add the right and left node

    if left_side_ is not False:
      #Whatever is needed for the extra rotation
      node.left = node.left.right
      node.left.right.left = node.left

    node.left = node
    node = node.left.right

  def _right_rotate(self, node, right_side_=False):
    
    if right_side_ is not False:
      node.right.left = node.right
      node.right = node.right.left.right

    node.right.left = node
    node = node.right

  # Main Functions
  def insert(self, number, node=None):

    if self.root == None:
      self.root = Node(number)  
      return
    
    if node == None:
      node = self.root
    
    if number < node.number:
      if node.left == None:
        new_node = Node(number)
        node.left = new_node

      self.insert(number, node.left)

    else:
      if node.right == None:
        new_node = Node(number)
        node.right = new_node

      self.insert(number, node.right)

    left_height, right_height = node._get_height()
    
    node.height = max(left_height, right_height)
    # Check balance factor (you are using the 
    # height of the node in the left - the one in the right )
    # 
    # Remenber that measure balance does too much, get height 
    height_difference = self._measure_balance_rule(node)



    # For rotation to happen the balance factor must 
    # be higher than one
    # There are four possible scenarios for the rotation
    if height_difference <= -2:
      # Here should roate right
      node._left_rotate() # This requires two variables, one is a node and the other 
    elif height_difference >= 2:
      # Here should rotate left
      node._right_rotate()





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