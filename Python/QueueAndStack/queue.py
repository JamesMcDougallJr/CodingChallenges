from collections import deque

class Queue:

  def __init__(self, lst=None):
    if lst is None:
      self.q = deque()
    else:
      self.q = deque(lst)

  def push(self, value):
    self.q.append(value)

  def top(self):
    return self.q[0]

  def pop(self):
    return self.q.popleft()

  def __len__(self):
    return len(self.q)

  def isEmpty(self):
    return len(self.q) == 0
