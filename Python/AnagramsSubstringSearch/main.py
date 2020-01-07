def numAnagramSubstrings(pattern, string):

  print('Full String: {0}\tPattern: {1}'.format(string,pattern))
  patternDict = {}

  # O(len(pattern))
  for char in pattern:
    patternDict[char] = 0
  matches = []
  i = 0

  # while we are within one len(pattern) from the end
  # O(len(string))
  while i < len(string) - len(pattern) + 1:
    firstChar = string[i]

    # look at len(pattern) number of characters
    # O(len(pattern))
    for j in range(len(pattern)):
      # O(1)
      if string[i+j] in patternDict:
        patternDict[string[i+j]] = 1

    # at this point, if the pattern is here, all in patterndict are 1s
    numMatches = 0
    for key in patternDict.keys():
      if patternDict[key] == 0:
        print('No Pattern in substring: {0}'.format(string[i:i+len(pattern)]))
      else:
        numMatches += 1

    # if we have found matches for each char in the pattern
    # O(1)
    if numMatches == len(pattern):
      matches.append((i, string[i:i+len(pattern)]))

    # O(1)
    if firstChar in patternDict:
      patternDict[firstChar] = 0
    i += 1

  return matches

if __name__=='__main__':
  testPattern = 'abcd'
  testString = 'bacdgabcda'
  print(numAnagramSubstrings(testPattern, testString))