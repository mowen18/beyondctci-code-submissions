# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def spanning_tree(graph):
  preds = {}
  visited = set()

  
  def visit(node):
    visited.add(node)
    for nbr in graph[node]:
      if nbr not in visited:
        preds[nbr] = node
        visit(nbr)
  visit(0)

  res = []
  for node1, node2 in preds.items():
    res.append([node2, node1])
  return res
