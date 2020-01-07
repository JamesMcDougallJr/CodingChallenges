import queue, stack

q = queue.Queue()
print('Queue Test:')
for i in range(100):
  q.push(i)
while not q.isEmpty():
  print(q.pop())

print('Stack Test')
stack = stack.Stack()
for i in range(100):
  stack.push(i)
while not stack.isEmpty():
  print(stack.pop())