# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def topo_sort(graph):
  V = len(graph)
  in_degree = [0 for _ in range(V)]
  for node in range(V):
    for nbr in graph[node]:
      in_degree[nbr] += 1
  degree_zero = []
  for node in range(V):
    if in_degree[node] == 0:
      degree_zero.append(node)
  topores = []
  while degree_zero:
    node = degree_zero.pop()
    topores.append(node)
    for nbr in graph[node]:
      in_degree[nbr] -= 1
      if in_degree[nbr] == 0:
        degree_zero.append(nbr)
  return topores

def parallel_compilation(seconds, imports):
  graph = [[] for _ in range(len(seconds))]
  for package in range(len(seconds)):
    for dep in imports[package]:
      graph[dep].append(package)
  toporder = topo_sort(graph)
  durations = {}
  for node in toporder:
    if node not in durations:
      durations[node] = seconds[node]
    for nbr in graph[node]:
      if nbr not in durations:
        durations[nbr] = 0
      durations[nbr] = max(durations[nbr], seconds[nbr] + durations[node])
  return max(durations.values())

