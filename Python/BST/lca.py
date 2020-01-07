import bst

def lca(root, v1, v2):
  v1Stack = []
  current = root
  while current.value != v1:
      v1Stack.append(current)
      if v1 < current.value:
          current = current.left
      else:
          current = current.right

  v2Stack = []
  current = root
  while current.value != v2:
      v2Stack.append(current)
      if v2 < current.value:
          current = current.left
      else:
          current = current.right

  if len(v1Stack) < len(v2Stack):
    shorter = v1Stack
    longer  = v2Stack
  else:
    shorter = v2Stack
    longer = v1Stack

  minShorterIndex = -1
  for val in range(len(shorter)):
    if shorter[val] in longer:
      minShorterIndex = val

  return shorter[minShorterIndex].value

if __name__=='__main__':
  # root = bst.Node(4)
  # root.left = bst.Node(2)
  # root.left.left = bst.Node(1)
  # root.left.right = bst.Node(3)
  # root.right = bst.Node(7)
  # root.right.left = bst.Node(6)
  # print(lca(root, 1,7))
  root = bst.Node(2)
  root.left = bst.Node(1)
  root.right = bst.Node(3)
  root.right.right = bst.Node(5)
  root.right.right.left = bst.Node(4)
  root.right.right.right = bst.Node(6)
  print(lca_rec(root, 4,6))