# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def is_reachable(edges, V, node1, node2):
    adj = [[] for _ in range(V)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    visited = set()
    visited.add(node1)
    def dfs(node):
        for nbr in adj[node]:
            if nbr not in visited:
                visited.add(nbr)
                dfs(nbr)
    dfs(node1)
    return node2 in visited

    
