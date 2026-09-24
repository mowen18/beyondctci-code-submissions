# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
from collections import deque
def path(graph, node1, node2):
  q = deque()
  q.append(node1)
  preds = {node1: None}
  def bfs():
    while q:
      node = q.popleft()
      for nbr in graph[node]:
        if nbr not in preds:
          preds[nbr] = node
          q.append(nbr)
  
  bfs()

  if node2 not in preds:
    return []
  path = [node2]
  while path[-1] != node1:
      path.append(preds[path[-1]])
  path.reverse()
  return path

