# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def toposort(graph):
  in_degree = [0 for _ in range(len(graph))]
  for node in range(len(graph)):
    for nbr in graph[node]:
      in_degree[nbr] += 1
  degree_zero = []
  for node in range(len(graph)):
    if in_degree[node] == 0:
      degree_zero.append(node)
  top_sort = []
  while degree_zero:
    node = degree_zero.pop()
    top_sort.append(node)
    for nbr in graph[node]:
      in_degree[nbr] -= 1
      if in_degree[nbr] == 0:
        degree_zero.append(nbr)
  return top_sort

def counting_paths(graph, start):
  toporder = toposort(graph)
  counts = [0 for _ in range(len(graph))]
  counts[start] = 1
  for node in toporder:
    for nbr in graph[node]:
      counts[nbr] += counts[node]
  return counts
