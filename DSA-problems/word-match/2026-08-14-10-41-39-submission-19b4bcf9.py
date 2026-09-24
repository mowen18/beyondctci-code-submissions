# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
class Node:
  def __init__(self):
    self.children = {}
    self.end = False

class WordMatcher:
  def __init__(self, dictionary):
    self.root = Node()
    
    for word in dictionary:
      self._insert(word)

  def _insert(self, wrd):
    node = self.root
    for c in wrd:
      if c not in node.children:
        node.children[c] = Node()
      node = node.children[c]
    node.end = True
  
  def _search(self, pattern, idx, node):
    if idx == len(pattern):
      return node.end
    c = pattern[idx]
    if c == "*":
      for child in node.children.values():
        if self._search(pattern, idx + 1, child):
          return True
      return False
    else:
      if c not in node.children:
        return False
      return self._search(pattern, idx + 1, node.children[c])
      
  def check(self, pattern):
    return self._search(pattern, 0, self.root)


  


