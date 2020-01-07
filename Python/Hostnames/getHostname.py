import re
def getHostname(s):
  hostnames = []
  splitOnHttp = s.split('http')
  for possibleHostname in splitOnHttp:
    scrubbed = testRegex(possibleHostname)
    if scrubbed:
      hostnames.append(scrubbed)
  return hostnames


def testRegex(s):
  startPattern = re.compile(r'(s|)://(www|ww2|)')
  matches = startPattern.search(s)
  if not matches:
    return False
  s = s[len(matches.group()):]
  splitOnDot = s.split('.')
  hostnameSubPattern = re.compile(r'[a-z0-9]+')

  # the last item in this list is an 'Ending thingy" so could have random stuff appended to it, we can remove. So remove it later
  finalHostname = []
  for subNameIndex in range(len(splitOnDot)):
    matches = hostnameSubPattern.search(splitOnDot[subNameIndex])
    if matches:
      if matches.group() == splitOnDot[subNameIndex]:
        finalHostname.append(matches.group())
      elif subNameIndex == len(splitOnDot)-1:
        finalHostname.append(matches.group())
  return '.'.join(finalHostname)


if __name__=='__main__':
  testString = 'http:james.com<http://hello.new>>><///http://hel98.new'
  #print(getHostname(testString))
  f = open('./test.txt')
  contents = f.read()
  print(getHostname(contents))