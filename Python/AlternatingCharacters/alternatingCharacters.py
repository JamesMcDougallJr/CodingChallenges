def alternatingCharacters(s):
  numDeletions = 0
  indicesToRemove = []
  previous = ''
  for index in range(len(s)):
      if previous == s[index]:
          numDeletions += 1
          indicesToRemove.append(index)
      previous = s[index]
  print(indicesToRemove)
  s = list(s)
  for index in indicesToRemove:
    s[index] = ''
  return (numDeletions,''.join(s))

if __name__=='__main__':
  print(alternatingCharacters('AAABBB'))
