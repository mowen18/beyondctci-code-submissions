# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
class UnionFind:
  def __init__(self):
    self.parent = {}
    self.groups = 0

  def add(self, x):
    if x in self.parent:
        return
    self.parent[x] = x
    self.groups  += 1

  def find(self, x):
    if x not in self.parent: return
    root = self.parent[x]
    while self.parent[root] != root:
        root = self.parent[root]
    return root

  def union(self, x, y):
    repr_x, repr_y = self.find(x), self.find(y)
    if repr_x == repr_y: return
    self.parent[repr_y] = repr_x
    self.groups -= 1

  def size(self):
    return len(self.parent)

  def num_groups(self):
    return self.groups
