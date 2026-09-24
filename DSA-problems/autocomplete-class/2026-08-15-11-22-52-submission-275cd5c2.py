# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
class Node:
    def __init__(self):
        self.children = {}
        self.end = False
class Trie:
  def __init__(self):
    self.root = Node()

  def insert(self, s):
    node = self.root
    for c in s:
        if c not in node.children:
            node.children[c] = Node()
        node = node.children[c]
    node.end = True

  def autocomplete(self, prefix):
    cur_node = self.root
    cur_string = []
    for c in prefix:
        if c not in cur_node.children:
            return []
        cur_node = cur_node.children[c]
        cur_string.append(c)
    res = []
    def dfs(node):
        if node.end:
            res.append(''.join(cur_string))
        for char, child in node.children.items():
            cur_string.append(char)
            dfs(child)
            cur_string.pop()
    
    dfs(cur_node)
    return res
            
        
        

