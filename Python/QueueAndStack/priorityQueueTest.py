import priorityQueue as pqueue
import random

def testIntegers():
  pq = pqueue.PriorityQueue()
  for i in range(10):
    pq.push(i)
  while not pq.isEmpty():
    print(pq.pop())

def testPoints(key=lambda x:x):
  pq = pqueue.PriorityQueue(key=key)
  for i in range(10):
    point = (random.randint(0,10), random.randint(0,10))
    pq.push(point)
  while not pq.isEmpty():
    point = pq.pop()
    print('Point: {0}\tDistance:{1}'.format(point, point[0]**2 + point[1]**2))

print('------Testing with lambda x:x------------')
testPoints(lambda x:x)
print('-----------Testing with lambda x: x[0]**2 + x[1]**2--------------')
testPoints(lambda x: x[0]**2 + x[1]**2)
print('-----------Testing with lambda x: - x[0]**2 - x[1]**2--------------')
testPoints(lambda x: -(x[0]**2) - (x[1]**2))