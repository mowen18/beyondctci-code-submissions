# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def num_connected_components_over_time(n, edges, times):
    graph = [[] for _ in range(n)]
    for n1, n2, wt in edges:
        graph[n1].append((n2, wt))
        graph[n2].append((n1, wt))
    
    #visited = set()
    def visit(node, time, visited):
        for nbr, wt in graph[node]:
            if nbr not in visited and wt <= time:
                visited.add(nbr)
                visit(nbr, time, visited)
    
    counts = []
    for tm in times:
        visited = set()
        cnt = 0
        for node in range(len(graph)):
            if node not in visited:
                visited.add(node)
                visit(node, tm, visited)
                cnt +=1
        counts.append(cnt)
        #visited.clear()
    return counts




