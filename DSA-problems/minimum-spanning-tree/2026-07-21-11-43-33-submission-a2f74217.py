# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import math, heapq
def minimum_spanning_tree(v, edges):
  adjlist = [[] for _ in range(v)]
  for n1, n2, w in edges:
    adjlist[n1].append((n2, w))
    adjlist[n2].append((n1, w))
  

  heap = [(0,0)]
  vis = set()
  dist = [math.inf for _ in range(v)]
  dist[0] = 0
  while heap:
    _, node = heapq.heappop(heap)
    if node in vis:
      continue
    
    vis.add(node)
    for neighbor, wt in adjlist[node]:
      if neighbor not in vis and wt < dist[neighbor]:
        dist[neighbor] = wt
        heapq.heappush(heap, (wt, neighbor))
  return sum(dist)


