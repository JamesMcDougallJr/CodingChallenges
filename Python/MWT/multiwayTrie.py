class Mwt(object):

  def __init__(self):
    self.rootNode = MwtNode()

  def insert(self, word):
    current = self.rootNode
    for char in word:
      # set the current node with the char and get that node in return
      current = current.setChar(char)
    current.terminate = True

  def contains(self, word):
    current = self.rootNode
    for char in word:
      if current is None:
        print('Char does not exist')
        return False

      nextNode = current.getChar(char)
      if nextNode is not None:
        print('Found Char {0}'.format(char))
      else:
        print('Char {0} not in the trie'.format(char))
      current = nextNode
    return current.terminate


class MwtNode(object):

  def __init__(self):
    self.chars = [None]*26
    self.terminate = False

  def setChar(self, char):
    self.chars[ord(char)-97] = MwtNode()
    return self.chars[ord(char)-97]

  def getChar(self, char):
    return self.chars[ord(char)-97]