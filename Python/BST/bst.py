class Node(object):
  def __init__(self, value, height=0):
    self.value = value
    self.left = None
    self.right = None
    self.height = height

  """
    Given a new value, insert it into its appropriate place in the tree with
    self as the root.
  """
def insert(root, value, level):
  if value < root.value:
    # then value is going in the left subtree
    if root.left is None:
      root.left = Node(value, height=level)
    else:
      insert(root.left, value, level+1)
  elif value >= root.value:
    if root.right is None:
      root.right = Node(value, height=level)
    else:
      insert(root.right,value, level+1)

def find(root,value):
  if root is None:
    return None
  if value == root.value:
    return root
  elif value < root.value:
    return find(root.left, value)
  elif value > root.value:
    return find(root.right, value)

def inorder(root):
  if root is not None:
    inorder(root.left)
    print(root.value)
    inorder(root.right)

def preorder(root):
  if root is not None:
    print(root.value)
    preorder(root.left)
    preorder(root.right)

def postorder(root):
  if root is not None:
    postorder(root.left)
    postorder(root.right)
    print(root.value)