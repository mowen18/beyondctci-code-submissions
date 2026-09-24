# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def highest_average_elevation_gain(V, edges):
  graph = [[] for _ in range(V)]
  for u, v, wt in edges:
    graph[u].append((v, wt))
    graph[v].append((u, wt))
  node_to_cc = {}
  conc = {}
  visited = set()
  def visit(node, cc):
    visited.add(node)
    node_to_cc[node] = cc
    for nbr, wt in graph[node]:
      if nbr not in visited:
        visit(nbr, cc)
  cc = 0
  for node in range(len(graph)):
    if node not in visited:
      conc[cc] = []
      visit(node, cc)
      cc += 1
  for u, v, wt in edges:
    comp = node_to_cc[u]
    conc[comp].append(wt)
  res = []
  for elevations in conc.values():
    if elevations:
      res.append(sum(elevations)/len(elevations))
  if not res: return 0
  return max(res)


  
