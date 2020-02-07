def most_frequent(lst):
  if len(lst) <= 0:
    return -1
  frequencies = {}
  for val in test1:
    ret = frequencies.get(val)
    if ret:
      frequencies[val] += 1
    else:
      frequencies[val] = 1
  maxVal = -1 # can't have -1 of something in the array
  maxKey = None
  for key,val in frequencies.items():
    if val > maxVal:
      maxVal = val
      maxKey = key
  return maxKey


test1 = [1, 1, 3, 2, 3, 1]
test2 = []
assert most_frequent(test1) == 1
assert most_frequent(test2) == -1