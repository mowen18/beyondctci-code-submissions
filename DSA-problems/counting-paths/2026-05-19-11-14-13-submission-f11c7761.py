# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def topsort(graph):
  V = len(graph)
  in_degree = [0 for _ in range(V)]
  for node in range(V):
    for nbr in graph[node]:
      in_degree[nbr] += 1
  degree_zero = []
  for node in range(V):
    if in_degree[node] == 0:
      degree_zero.append(node)
  top = []
  while degree_zero:
    node = degree_zero.pop()
    top.append(node)
    for nbr in graph[node]:
      in_degree[nbr] -= 1
      if in_degree[nbr] == 0:
        degree_zero.append(nbr)
  return top

def counting_paths(graph, start):
  top = topsort(graph)
  paths = [0 for _ in range(len(graph))]
  paths[start] = 1
  for node in top:
    for nbr in graph[node]:
      paths[nbr] += paths[node]
  return paths
  
