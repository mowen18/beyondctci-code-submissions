# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.

def path(graph, node1, node2):
  preds = {node2: None}
  def dfs(graph):
    stack = [node2]
    while stack:
      node = stack.pop()
      for nbr in graph[node]:
        if nbr not in preds:
          preds[nbr] = node
          stack.append(nbr)
  dfs(graph)
  if node1 not in preds:
    return []
  path = [node1]
  while path[-1] != node2:
    path.append(preds[path[-1]])
  return path
  
  
