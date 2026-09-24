# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def spanning_tree(graph):
    preds = {}
    visited = set()
    def dfs(node):
      visited.add(node)
      for nbr in graph[node]:
        if nbr not in visited:
          preds[nbr] = node
          dfs(nbr)
    dfs(0)
    tree = []
    for node, pred in preds.items():
      tree.append([pred, node])
    return tree

      

