class Stack:
  def __init__(self, lst=None):
    if lst is None:
      self.stack = []
    else:
      self.stack = lst

  def __len__(self):
    return len(self.stack)

  def push(self,value):
    self.stack.append(value)

  def pop(self):
    return self.stack.pop()

  def isEmpty(self):
    return len(self.stack) == 0