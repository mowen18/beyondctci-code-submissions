# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def spanning_tree(graph):
  visited = set()
  preds = {0: None}
  def dfs(node):
    #visited.add(node)
    #preds[]
    for nbr in graph[node]:
      if nbr not in preds:
        preds[nbr] = node
        dfs(nbr)
  preds = {0: None}
  dfs(0)
  edges = []
  for node, pred in preds.items():
    if pred == None: continue
    edges.append([pred, node])
  return edges



  
