class Sorter(object):

  @classmethod
  def _merge(cls, left, right):
    l = 0
    r = 0
    merged = []
    while l < len(left) and r < len(right):
      if left[l] <= right[r]:
        merged.append(left[l])
        l += 1
      else:
        merged.append(right[r])
        r += 1
    while l < len(left):
      merged.append(left[l])
      l += 1
    while r < len(right):
      merged.append(right[r])
      r += 1
    return merged


  @classmethod
  def mergeSort(cls, lst):
    print(lst)
    if len(lst) <= 1:
      return lst
    leftHalf = lst[:len(lst)//2]
    rightHalf = lst[len(lst)//2:]
    leftHalf = Sorter.mergeSort(leftHalf)
    rightHalf = Sorter.mergeSort(rightHalf)
    return Sorter._merge(leftHalf, rightHalf)
  

  @classmethod
  def _partition(cls, lst,low,high):
    i = low - 1
    pivot = lst[high]
    for j in range(low,high):
      if lst[j] <= pivot:
        i += 1
        lst[i], lst[j] = lst[j], lst[i]
    lst[i+1], lst[high] = lst[high], lst[i+1]
    return i+1

  @classmethod
  def _quickSortHelper(cls, lst, low, high):
    if low < high:
      partitionIndex = Sorter._partition(lst, low, high)
      Sorter._quickSortHelper(lst,low,partitionIndex-1)
      Sorter._quickSortHelper(lst, partitionIndex+1, high)
    return lst

  @classmethod
  def quickSort(cls, lst):
    print(lst)
    return Sorter._quickSortHelper(lst, 0, len(lst)-1)



if __name__ =='__main__':
  print(Sorter.mergeSort([1,4,2,9,7,10,6]))
  print(Sorter.quickSort([1,4,2,9,7,10,6]))