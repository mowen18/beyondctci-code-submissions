# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
from collections import deque
def all_infected(graph, infected):
  queue = deque()
  distances = {}
  for node in infected:
    queue.append(node)
    distances[node] = 0
  
  while queue:
    node = queue.popleft()
    for nbr in graph[node]:
      if nbr not in distances:
        distances[nbr] = distances[node] + 1
        queue.append(nbr)
  
  return max(distances.values())
  
