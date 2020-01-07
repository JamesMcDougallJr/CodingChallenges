import heapq
class PriorityQueue(object):
  def __init__(self, lst=None, key=lambda x: x):
    self.key = key
    if lst is None:
      self.pq = []
    else:
      # perform the key function on each item in the list,
      # heapq will sort by this first element on insertion
      self.pq = [(key(item), item) for item in lst]
      self.pq = heapq.heapify(self.pq)

  def push(self, value):
    heapq.heappush(self.pq, (self.key(value), value))

  def pop(self):
    return heapq.heappop(self.pq)[1]

  def isEmpty(self):
    return len(self.pq) == 0
