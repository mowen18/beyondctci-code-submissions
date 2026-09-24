# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
from collections import deque
def all_infected(graph, infected):
  dist = {}
  q = deque()
  for node in infected:
    dist[node] = 0
    q.append(node)
  while q:
    node = q.popleft()
    for nbr in graph[node]:
      if nbr not in dist:
        dist[nbr] = 1 + dist[node]
        q.append(nbr)
  
  return max(dist.values())


  

