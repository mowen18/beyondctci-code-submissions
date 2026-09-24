# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
class UnionFind:
  def __init__(self):
    self.parent = {}
    self.size = {}

  # Assumes x is not already in the UnionFind.
  def add(self, x):
    self.parent[x] = x
    self.size[x] = 1

  # Assumes x is already in the UnionFind.
  def find(self, x):
    root = self.parent[x]
    while self.parent[root] != root:
      root = self.parent[root]
    while x != root:
      self.parent[x], x = root, self.parent[x]
    return root

  # Assumes x and y are already in the UnionFind.
  def union(self, x, y):
    repr_x, repr_y = self.find(x), self.find(y)
    if repr_x == repr_y:
      return  # They are already in the same set.
    if self.size[repr_x] < self.size[repr_y]:
      self.size[repr_y] += self.size[repr_x]
      self.parent[repr_x] = repr_y
    else:
      self.size[repr_x] += self.size[repr_y]
      self.parent[repr_y] = repr_x

def mst_reconstruction(v, edges):
  V = v
  uf = UnionFind()
  for u in range(V):
    uf.add(u)
  mst_edges = []
  edges.sort(key=lambda edge: edge[2])
  for u, v, weight in edges:
    repr_u, repr_v = uf.find(u), uf.find(v)
    if repr_u != repr_v:
      uf.union(u, v)
      mst_edges.append([u, v, weight])

  if len(mst_edges) == V - 1:
    return mst_edges
  return []  # The graph was not connected.


"""import math, heapq
def mst_reconstruction(v, edges):
  adjlist = [[] for _ in range(v)]
  for n1, n2, w in edges:
    adjlist[n1].append((n2, w))
    adjlist[n2].append((n1, w))
  

  minedges = [math.inf for _ in range(v)]
  minedges[0] = 0
  pq = [(0,0)]
  mst_cost = 0
  vis = [False for _ in range(v)]
  arr = []
  parent = [-1 for _ in range(v)]
  visited_count = 0
  while pq:
    w, u = heapq.heappop(pq)

    if vis[u]:
      continue
    vis[u] = True
    visited_count += 1
    mst_cost += minedges[u]
    if parent[u] != -1:
      arr.append([parent[u], u, w])
    for v, w in adjlist[u]:
      if not vis[v] and w < minedges[v]:
        minedges[v] = w
        parent[v] = u
        heapq.heappush(pq, (w, v))
  if visited_count != len(adjlist):
    return []
  return arr
  """

  
