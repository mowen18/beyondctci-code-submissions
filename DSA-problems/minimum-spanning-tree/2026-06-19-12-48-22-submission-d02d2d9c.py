# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import heapq
def minimum_spanning_tree(v, edges):
  adj = [[] for _ in range(v)]
  for n1, n2, w in edges:
    adj[n1].append((n2, w))
    adj[n2].append((n1, w))
  
  heap = [(0,0)]
  total = 0
  visited = set()
  while heap and len(heap) < v:
    wt, node = heapq.heappop(heap)
    if node in visited:
      continue
    visited.add(node)
    total += wt
    for nbr, wt in adj[node]:
      if nbr not in visited:
        heapq.heappush(heap, (wt, nbr))
  return total


