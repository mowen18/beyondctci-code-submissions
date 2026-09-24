# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
class Node:
  def __init__(self):
    self.children = {}
    self.isEnd = False

class Trie:
  def __init__(self):
    self.root = Node()

  def insert(self, s):
    current = self.root
    for char in s:
      if char not in current.children:
        current.children[char] = Node()
      current = current.children[char]
    current.isEnd = True

  def contains(self, s):
    current = self.root
    for char in s:
      if char not in current.children:
        return False
      current = current.children[char]
    return current.isEnd

  def remove(self, s):

    def remove_rec(node, i):
      if i == len(s):
        if not node.isEnd:
          return False
        node.isEnd = False
        return len(node.children) == 0
      
      if s[i] not in node.children:
        return False
      should_delete = remove_rec(node.children[s[i]], i + 1)
      if should_delete:
        del node.children[s[i]]
        return node.isEnd == False and len(node.children) == 0
      return False
    remove_rec(self.root, 0)
    
    
