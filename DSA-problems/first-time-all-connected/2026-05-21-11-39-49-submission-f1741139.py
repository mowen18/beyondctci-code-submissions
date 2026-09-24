# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def visit(graph, visited, node):
  for nbr in graph[node]:
    if nbr not in visited:
      visited.add(nbr)
      visit(graph, visited, nbr)

def is_before(cable_index, V, cables):
  graph = [[] for _ in range(V)]
  for i in range(cable_index + 1):
    node1, node2 = cables[i]
    graph[node1].append(node2)
    graph[node2].append(node1)
  
  visited = {0}
  visit(graph, visited, 0)
  return len(visited) < V

def first_time_all_connected_union_find(V, cables):
  l, r = 0, len(cables) - 1
  if is_before(r, V, cables):
    return -1

  while r - l > 1:
    mid = l + (r - l) // 2
    if is_before(mid, V, cables):
      l = mid
    else:
      r = mid
  return r





  
