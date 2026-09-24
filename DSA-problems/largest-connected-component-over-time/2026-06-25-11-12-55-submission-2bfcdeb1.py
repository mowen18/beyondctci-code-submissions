# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def largest_connected_component_over_time(n, edges, times):
    graph = [[] for _ in range(n)]
    for u, v, time in edges:
        graph[u].append((v, time))
        graph[v].append((u, time))
    
    def visit(node, time):
        cc = 1
        for nbr, tm in graph[node]:
            if nbr not in visited and tm <= time:
                visited.add(nbr)
                cc += visit(nbr, time)
        return cc
    res = []
    for t in times:
        visited = set()
        largestcc = 0
        ccsize = 0
        for node in range(len(graph)):
            if node not in visited:
                visited.add(node)
                ccsize = visit(node, t)
                largestcc = max(largestcc, ccsize)
                
        res.append(largestcc)
    return res


