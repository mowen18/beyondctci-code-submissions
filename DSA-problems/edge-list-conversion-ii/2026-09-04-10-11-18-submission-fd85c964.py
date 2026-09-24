# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def edge_list_to_adjacency_matrix(edges, V):
  adjlist = [[0] * V for _ in range(V)]
  for i, j in edges:
    adjlist[i][j] = 1
    adjlist[j][i] = 1
  return adjlist

