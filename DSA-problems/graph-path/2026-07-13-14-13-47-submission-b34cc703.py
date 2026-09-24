# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def path(graph, node1, node2):
  preds = {}
  def dfs(node):

    for nbr in graph[node]:
      if nbr not in preds:
        preds[nbr] = node
        dfs(nbr)
  
  preds[node1] = None
  dfs(node1)

  if node2 not in preds:
    return []
  path = [node2]
  while path[-1] != node1:
      path.append(preds[path[-1]])
  path.reverse()
  return path

