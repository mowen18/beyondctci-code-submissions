# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def topsort(graph):
  V = len(graph)
  indegree = [0 for _ in range(V)]
  for node in range(V):
    for nbr, _ in graph[node]:
      indegree[nbr] += 1
  degree_zero = []
  for node in range(V):
    if indegree[node] == 0:
      degree_zero.append(node)
  top = []
  while degree_zero:
    node = degree_zero.pop()
    top.append(node)
    for nbr, _ in graph[node]:
      indegree[nbr] -= 1
      if indegree[nbr] == 0:
        degree_zero.append(nbr)
  return top

def dag_distances(graph, start):
  topgraph = topsort(graph)
  distances = {start: 0}
  for node in topgraph:
    if node not in distances: continue
    for nbr, wt in graph[node]:
      if nbr not in distances or distances[node] + wt < distances[nbr]:
        distances[nbr] = distances[node] + wt
  res = []
  for node in range(len(graph)):
    if node not in distances:
      res.append(None)
    else:
      res.append(distances[node])
  return res


