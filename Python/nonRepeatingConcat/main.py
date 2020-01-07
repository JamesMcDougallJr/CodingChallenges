"""
  Find the number of unique strings that can be made from concatenations of the input.
  Strings must not have repeating characters.
"""
def numNonRepeatingConcats(lst):
  concatenations = []
  for s1 in range(len(lst)):
    for s2 in range(s1+1, len(lst)):
      concatenations.append(lst[s1]+lst[s2])
      concatenations.append(lst[s2]+lst[s1])

  numValid = 0
  validConcats = []
  for concatenation in concatenations:
    if noRepeats(concatenation):
      numValid += 1
      validConcats.append(concatenation)
  return validConcats

def noRepeats(string):
  chars = {}
  for char in string:
    if char in chars:
      return False
    else:
      chars[char] = True
  return True

def canConcat(str1, str2):
  for char in str1:
    if char in str2:
      return False
  return True

if __name__=='__main__':
  test = ['co', 'dil','ity']
  print(numNonRepeatingConcats(test))