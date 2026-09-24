# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
from collections import deque
def bfs(graph, sources):
    q = deque()
    distances = {}
    for startnode in sources:
        q.append(startnode)
        distances[startnode] = 0
    while q:
        node = q.popleft()
        for nbr in graph[node]:
            if nbr not in distances:
                distances[nbr] = distances[node] + 1
                q.append(nbr)
    return distances
def all_infected(graph, infected):
    res = bfs(graph, infected)
    return max(res.values())

