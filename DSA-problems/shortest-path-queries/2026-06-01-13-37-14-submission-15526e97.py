# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
from collections import deque
def shortest_path_queries(graph, start, queries):
  q = deque()
  q.append(start)
  preds = {start: None}
  while q:
    node = q.popleft()
    for nbr in graph[node]:
      if nbr not in preds:
        preds[nbr] = node
        q.append(nbr)
  res = []
  for target in queries:
    if target not in preds:
      res.append([])
    else:
      path = [target]
      while path[-1] != start:
        path.append(preds[path[-1]])
      path.reverse()
      res.append(path)
  return res

    

