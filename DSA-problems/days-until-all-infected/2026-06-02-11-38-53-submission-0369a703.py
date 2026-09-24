# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
from collections import deque
def all_infected(graph, infected):

  q = deque()
  dist = {}
  for start in infected:
    q.append(start)
    dist[start] = 0
  
  while q:
    node = q.popleft()
    for nbr in graph[node]:
      if nbr not in dist:
        dist[nbr] = dist[node] + 1
        q.append(nbr)
  
  return(max(dist.values()))
  

  

