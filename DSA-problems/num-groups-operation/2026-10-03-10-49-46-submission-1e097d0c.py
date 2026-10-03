# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
class CustomUnionFind:
  def __init__(self):
    self.parent = {}
    self.gsize = {}
    self.groups = 0

  def add(self, x):
    self.parent[x] = x
    self.gsize[x] = 1
    self.groups += 1

  def find(self, x):
    if x not in self.parent: return
    root = self.parent[x]
    while self.parent[root] != root:
      root = self.parent[root]
    while x != root:
      self.parent[x], x = root, self.parent[x]
    
    return root
    

  def union(self, x, y):
    repx, repy = self.find(x), self.find(y)
    if repx == repy: return
    if self.gsize[repx] <= self.gsize[repy]:
      self.gsize[repy] += self.gsize[repx]
      self.parent[repy] = repx
    else:
      self.gsize[repx] += self.gsize[repy]
      self.parent[repx] = repy
    self.groups -= 1


  def size(self):
    return len(self.parent)

  def num_groups(self):
    return self.groups
