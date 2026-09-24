# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def edge_list_to_adjacency_list(edges, V):
  adjlist = [[] for _ in range(V)]
  for n1, n2 in edges:
    adjlist[n1].append(n2)
    adjlist[n2].append(n1)
  return adjlist
