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


def parallel_compilation(seconds, imports):
  graph = [[] for _ in range(len(seconds))]
  for node in range(len(seconds)):
    for nbr in imports[node]:
      graph[nbr].append(node)

  top = topsort(graph)
  res = {}
  mmax = 0
  for node in top:
    if node not in res:
      res[node] = seconds[node]
    for nbr in graph[node]:
      if nbr not in res:
        res[nbr] = 0
      res[nbr] = max(res[nbr], seconds[nbr] + res[node])
  return max(res.values())


  
