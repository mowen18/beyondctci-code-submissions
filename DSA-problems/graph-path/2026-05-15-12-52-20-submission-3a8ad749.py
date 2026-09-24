# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def path(graph, node1, node2):
  preds = {node2: None}
  
  def visit(node):
    for nbr in graph[node]:
      if nbr not in preds:
        preds[nbr] = node
        visit(nbr)
  
  visit(node2)

  path = [node1]
  if node1 not in preds:
    return []
  while path[-1] != node2:
    path.append(preds[path[-1]])
  return path


