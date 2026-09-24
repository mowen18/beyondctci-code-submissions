# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
from collections import deque

def shortest_path_queries(graph, start, queries):
    queue = deque()
    queue.append(start)
    preds = {start: None}

    while queue:
      node = queue.popleft()
      for nbr in graph[node]:
        if nbr not in preds:
          preds[nbr] = node
          queue.append(nbr)
    res = []
    for node in queries:
      if node not in preds:
        res.append([])
      else:
        path = []
        cur = node
        while cur != None:
          path.append(cur)
          cur = preds[cur]
        res.append(path[::-1])
    return res

