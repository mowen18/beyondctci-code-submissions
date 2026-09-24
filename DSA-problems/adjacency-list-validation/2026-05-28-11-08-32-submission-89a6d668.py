# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def validate(graph):
  V = len(graph)
  for node in range(V):
    seen = set()
    for nbr in graph[node]:
      if nbr < 0 or nbr >= V:
        return False
      if nbr == node:
        return False
      if nbr in seen:
        return False
      seen.add(nbr)
  res = set()
  for node in range(V):
    for nbr in graph[node]:
      node1, node2 = max(node, nbr), min(node, nbr)
      edge = (node1, node2)
      if edge in res:
        res.remove(edge)
      else:
        res.add(edge)
  return len(res) == 0



