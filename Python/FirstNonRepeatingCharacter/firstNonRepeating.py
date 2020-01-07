def firstNonRepeat(string):
  repeats = {}
  for char in string:
    if char in repeats:
      return char
    else:
      repeats[char] = 1

if __name__ == '__main__':
  testString = 'agcdefccb'
  print(firstNonRepeat(testString))