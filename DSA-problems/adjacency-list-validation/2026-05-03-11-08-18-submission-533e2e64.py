# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def validate(graph):
    V = len(graph)
    for node in range(V):
      seen = set()
      for nbr in graph[node]:
        if nbr < 0 or nbr >= V: return False
        if nbr in seen: return False
        if nbr == node: return False
        seen.add(nbr)
    edges = set()
    for node1 in range(V):
      for node2 in graph[node1]:
        edge = (min(node1, node2), max(node1, node2))
        if edge in edges:
          edges.remove(edge)
        else:
          edges.add(edge)
    return len(edges) == 0


