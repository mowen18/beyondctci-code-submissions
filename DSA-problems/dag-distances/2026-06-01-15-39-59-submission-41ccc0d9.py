# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def dag_distances(graph, start):
  
  def topsort(graph):
    in_deg = [0 for _ in range(len(graph))]
    for node in range(len(graph)):
      for nbr, _ in graph[node]:
        in_deg[nbr] += 1

    degzero = []
    for node in range(len(graph)):
      if in_deg[node] == 0:
        degzero.append(node)
    top = []
    while degzero:
      node = degzero.pop()
      top.append(node)
      for nbr, _ in graph[node]:
        in_deg[nbr] -= 1
        if in_deg[nbr] == 0:
          degzero.append(nbr)
    
    return top


  topgraph = topsort(graph)
  distances = {start: 0}
  for node in topgraph:
    if node not in distances: continue
    for nbr, weight in graph[node]:
      if nbr not in distances or distances[node] + weight < distances[nbr]:
        distances[nbr] = distances[node] + weight
  res = []

  for node in range(len(graph)):
    if node not in distances:
      res.append(None)
    else:
      res.append(distances[node])
  return res
  

        

