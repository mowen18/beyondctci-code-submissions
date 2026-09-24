# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def topological_sort(graph):
  in_degree = [0 for _ in range(len(graph))]
  n = len(graph)
  for node in range(n):
    for nbr in graph[node]:
      in_degree[nbr] += 1
  
  deg_zero = []
  for node in range(n):
    if in_degree[node] == 0:
      deg_zero.append(node)
  
  topsort = []
  while deg_zero:
    node = deg_zero.pop()
    topsort.append(node)
    for nbr in graph[node]:
      in_degree[nbr] -= 1
      if in_degree[nbr] == 0:
        deg_zero.append(nbr)
  
  if len(topsort) != n:
    return []
  return topsort
