# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
class Node:
  def __init__(self):
    self.children = {}
    self.end = False

class Trie:
  def __init__(self):
    self.root = Node()

  def insert(self, s):
    curnode = self.root
    for char in s:
      if char not in curnode.children:
        curnode.children[char] = Node()
      curnode = curnode.children[char]
    curnode.end = True

  def contains(self, s):
    curnode = self.root
    for char in s:
      if char not in curnode.children: 
        return False
      curnode = curnode.children[char]
    if curnode.end: return True
    return False


  def remove(self, s):
    
    def remove_rec(node, i):

      if i == len(s):
        if node.end:
          node.end = False
          if len(node.children) == 0:
            return True
        return False
      
      if s[i] not in node.children:
        return False
      
      should_delete = remove_rec(node.children[s[i]], i + 1)

      if should_delete:
        del node.children[s[i]]
        return node.end == False and len(node.children) == 0
      return False
    remove_rec(self.root, 0)














