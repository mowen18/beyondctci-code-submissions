# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def dag_neighbors(graph, node):
  return [nbr for nbr in graph[node] if len(graph[nbr]) > len(graph[node])]

def toposort(graph):
  V = len(graph)
  indegree = [0 for _ in range(V)]
  for node in range(V):
    for nbr in dag_neighbors(graph, node):
      indegree[nbr] += 1
  degree_zero = []
  for node in range(V):
    if indegree[node] == 0:
      degree_zero.append(node)
  topo = []
  while degree_zero:
    node = degree_zero.pop()
    topo.append(node)
    for nbr in dag_neighbors(graph, node):
      indegree[nbr] -= 1
      if indegree[nbr] == 0:
        degree_zero.append(nbr)
  return topo


def longest_path_of_increasing_degrees(v, edges):
  graph = [[] for _ in range(v)]
  for i, j in edges:
    graph[i].append(j)
    graph[j].append(i)
  topgraph = toposort(graph)
  lengths = {i: 0 for i in range(v)}
  for node in topgraph:
    for nbr in dag_neighbors(graph, node):
      lengths[nbr] = max(lengths[nbr], lengths[node] + 1)
  return max(lengths.values())
