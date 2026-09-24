# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def dag_path_reconstruction(graph, start, goal):
  
  def topsort(graph):
    indeg = [0 for _ in range(len(graph))]
    for node in range(len(graph)):
      for nbr, _ in graph[node]:
        indeg[nbr] += 1
    
    degzero = []
    for node in range(len(graph)):
      if indeg[node] == 0:
        degzero.append(node)
    top = []
    while degzero:
      node = degzero.pop()
      top.append(node)
      for nbr, _ in graph[node]:
        indeg[nbr] -= 1
        if indeg[nbr] == 0:
          degzero.append(nbr)
    return top

  topordering = topsort(graph)
  preds = {start: None}
  dist = {start: 0}
  res = [0 for _ in range(len(graph))]
  for node in topordering:
    if node not in dist: continue
    for nbr, wt in graph[node]:
      if nbr not in dist or dist[node] + wt < dist[nbr]:
        dist[nbr] = dist[node] + wt
        preds[nbr] = node
  if goal not in preds: return []
  if start == goal: return [start]
  path = [goal]
  while path[-1] != start:
    path.append(preds[path[-1]])
  path.reverse()
  return path



