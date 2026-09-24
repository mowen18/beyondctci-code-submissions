# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def dag_distances(graph, start):
    
  def topsort(graph):
    V = len(graph)
    indeg = [0 for _ in range(len(graph))]
    for node in range(V):
      for nbr, wt in graph[node]:
        indeg[nbr] += 1
    degzero = []
    for node in range(V):
      if indeg[node] == 0:
        degzero.append(node)
    top = []
    while degzero:
      node = degzero.pop()
      top.append(node)
      for nbr, wt in graph[node]:
        indeg[nbr] -= 1
        if indeg[nbr] == 0:
          degzero.append(nbr)
    return top
  
  toporder = topsort(graph)

  dist = {start: 0}
  for node in toporder:
    if node not in dist: continue
    for nbr, wt in graph[node]:
      if nbr not in dist or dist[node] + wt < dist[nbr]:
        dist[nbr] = dist[node] + wt
  res = []
  for node in range(len(graph)):
    if node not in dist:
      res.append(None)
    else:
      res.append(dist[node])
  return res


