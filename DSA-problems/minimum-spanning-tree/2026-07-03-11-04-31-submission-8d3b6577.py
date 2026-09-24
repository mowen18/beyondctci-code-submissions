# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import math, heapq
def minimum_spanning_tree(v, edges):
  adjlist = [[] for _ in range(v)]
  for u, x, w in edges:
    adjlist[u].append((x, w))
    adjlist[x].append((u, w))
  
  minedge = [math.inf for _ in range(v)]
  minedge[0] = 0
  vis = [False for _ in range(v)]
  mst_cost = 0
  pq = [(0,0)]
  while pq:
    _, u = heapq.heappop(pq)

    if vis[u]:
      continue
    vis[u] = True
    mst_cost += minedge[u]
    for v, w in adjlist[u]:
      if not vis[v] and w < minedge[v]:
        minedge[v] = w
        heapq.heappush(pq, (w, v))
  return mst_cost



