
def longestCommonSubstring(string1, string2):

  suffixes = [[0 for k in range(len(string2)+1)] for l in range(len(string1)+1)]

  longest = 0

  for i in range(len(string1)+1):
    for j in range(len(string2)+1):
      if i == 0 or j == 0:
        suffixes[i][j] = 0
      elif string1[i-1] == string2[j-1]:
        suffixes[i][j] = suffixes[i-1][j-1] + 1
        longest = max(longest, suffixes[i][j])
      else:
        suffixes[i][j] = 0
  return longest



if __name__ =='__main__':
  print(longestCommonSubstring('OldSite:GeeksforGeeks.org', 'NewSite:GeeksQuiz.com'))