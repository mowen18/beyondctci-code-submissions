# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def dag_distances(graph, start):
  
  def topsort(graph):
    indegree = [0 for _ in range(len(graph))]
    for node in range(len(graph)):
      for nbr, _ in graph[node]:
        indegree[nbr] += 1
    degreezero = []
    for node in range(len(graph)):
      if indegree[node] == 0:
        degreezero.append(node)
    
    top = []
    while degreezero:
      node = degreezero.pop()
      top.append(node)
      for nbr, _ in graph[node]:
        indegree[nbr] -= 1
        if indegree[nbr] == 0:
          degreezero.append(nbr)
    return top
  
  topgraph = topsort(graph)
  distances = {start: 0}
  for node in topgraph:
    if node not in distances: continue
    for nbr, wt in graph[node]:
      if nbr not in distances or distances[node] + wt < distances[nbr]:
        distances[nbr] = distances[node] + wt

  res = []
  for node in range(len(graph)):
    if node in distances:
      res.append(distances[node])
    else:
      res.append(None)
  return res

