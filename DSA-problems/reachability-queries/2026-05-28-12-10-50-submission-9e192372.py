# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def connected_component_queries(graph, queries):
  cc = {}
  seen = set()
  def visit(node, comp):
    cc[node] = comp
    for nbr in graph[node]:
      if nbr not in cc:
        cc[nbr] = comp
        visit(nbr, comp)
  comp = 0
  for node in range(len(graph)):
    if node not in cc:
      visit(node, comp)
      comp += 1
  res= []
  for node1, node2 in queries:
    res.append(cc[node1] == cc[node2])
  return res
  



