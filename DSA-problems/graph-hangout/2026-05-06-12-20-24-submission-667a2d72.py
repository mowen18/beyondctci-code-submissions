# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
from collections import deque
import math
def walking_distance_to_coffee(graph, node1, node2, node3):
    def bfs(node_start):
      queue = deque()
      distances = {node_start: 0}
      queue.append(node_start)
      while queue:
        node = queue.popleft()
        for nbr in graph[node]:
          if nbr not in distances:
            distances[nbr] = distances[node] + 1
            queue.append(nbr)
      return distances
    distances1 = bfs(node1)
    distances2 = bfs(node2)
    distances3 = bfs(node3)
    res = math.inf
    for i in range(len(graph)):
      res = min(res, distances1[i] + distances2[i] + distances3[i])
    return res


