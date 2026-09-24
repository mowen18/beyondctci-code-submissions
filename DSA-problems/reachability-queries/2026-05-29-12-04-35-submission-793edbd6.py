# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def connected_component_queries(graph, queries):
  connected_comp = {}
  def visit(node, cc):
    connected_comp[node] = cc
    for nbr in graph[node]:
      if nbr not in connected_comp:
        visit(nbr, cc)
  
  cc = 0
  for node in range(len(graph)):
    if node not in connected_comp:
      visit(node, cc)
      cc += 1
  res = []
  for node1, node2 in queries:
    res.append(connected_comp[node1] == connected_comp[node2])
  return res






