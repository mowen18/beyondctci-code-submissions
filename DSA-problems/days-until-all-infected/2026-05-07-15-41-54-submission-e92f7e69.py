# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
from collections import deque
def all_infected(graph, infected):
  queue = deque()
  distances = {}
  for nodestart in infected:
    distances[nodestart] = 0
    queue.append(nodestart)
  while queue:
    node = queue.popleft()
    for nbr in graph[node]:
      if nbr not in distances:
        distances[nbr] = distances[node] + 1
        queue.append(nbr)
  return max(distances.values())
  


