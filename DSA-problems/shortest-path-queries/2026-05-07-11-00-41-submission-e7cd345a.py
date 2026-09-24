# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
from collections import deque
def shortest_path_queries(graph, start, queries):
    queue = deque()
    preds = {start: None}
    queue.append(start)
    while queue:
      node = queue.popleft()
      for nbr in graph[node]:
        if nbr not in preds:
          preds[nbr] = node
          queue.append(nbr)
    res = []
    for targetnode in queries:
      if targetnode not in preds:
        res.append([])
      else:
        cur = [targetnode]
        while cur[-1] != start:
          cur.append(preds[cur[-1]])
        res.append(cur[::-1])
    return res
      


