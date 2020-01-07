import bst
import random, time
def testRandomInsert():
  root = bst.Node(random.randint(0,1000))
  start = time.time()
  for i in range(100000):
    bst.insert(root, random.randint(0,1000), 0)

  end = time.time()
  print('Time Elapsed: {0}\tAverage Time per insert: {1}'.format(end-start, (end-start)/100000))
def testInOrderInsert():
  root = bst.Node(500)
  for i in range(1000):
    bst.insert(root, i, 0)

  if bst.find(root, 100) is None:
    print("Shouldn't be None")
  else:
    print('Found 100')
  bst.inorder(root)

def testHeight():
  root = bst.Node(500)
  for i in range(1000):
    bst.insert(root, i, 0)
  print(bst.find(root,199).height)

if __name__=='__main__':
  testHeight()