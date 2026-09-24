# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def dag_distances(graph, start):
  
  def topsort(graph):
    indeg = [0 for _ in range(len(graph))]
    for node in range(len(graph)):
      for nbr, wt in graph[node]:
        indeg[nbr] += 1
    degz = []
    for node in range(len(graph)):
      if indeg[node] == 0:
        degz.append(node)
    topgraph = []
    while degz:
      node = degz.pop()
      topgraph.append(node)
      for nbr, _ in graph[node]:
        indeg[nbr] -= 1
        if indeg[nbr] == 0:
          degz.append(nbr)
    return topgraph
  
  top = topsort(graph)
  distances = {start: 0}
  for node in top:
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





    


