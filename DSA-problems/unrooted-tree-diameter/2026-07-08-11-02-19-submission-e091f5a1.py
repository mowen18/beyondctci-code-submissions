# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def unrooted_tree_diameter(n, edges):
  adjlist = [[] for _ in range(n)]
  for u, v in edges:
    adjlist[u].append(v)
    adjlist[v].append(u)
  def dfs(node, dist):

    for nbr in adjlist[node]:
      if nbr not in dist:
        dist[nbr] = dist[node] + 1
        dfs(nbr, dist)
  
  dist1 = {0: 0}
  dfs(0, dist1)

  node2 = max(dist1, key=dist1.get)
  dist2 = {node2: 0}
  dfs(node2, dist2)
  diam = max(dist2.values())
  return diam



    