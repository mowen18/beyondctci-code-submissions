# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def topo_sort(graph):
  V = len(graph)
  in_degree = [0 for _ in range(V)]
  for node in range(V):
    for nbr, _ in graph[node]:
      in_degree[nbr] += 1
  degree_zero = []
  for node in range(V):
    if in_degree[node] == 0:
      degree_zero.append(node)
  topo = []
  while degree_zero:
    node = degree_zero.pop()
    topo.append(node)
    for nbr, _ in graph[node]:
      in_degree[nbr] -= 1
      if in_degree[nbr] == 0:
        degree_zero.append(nbr)
  if len(topo) < V:
    return []
  return topo
def dag_longest_path(graph, start):
  top = topo_sort(graph)
  dist = {start: 0}
  for node in top:
    if node not in dist:
      continue
    for nbr, wt in graph[node]:
      if nbr not in dist or dist[node] + wt > dist[nbr]:
        dist[nbr] = dist[node] + wt
  res = []
  for i in range(len(graph)):
    if i in dist:
      res.append(dist[i])
    else:
      res.append(None)
  return res
  
  
