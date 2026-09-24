# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def visit(visited, graph, node):
    for nbr in graph[node]:
        if nbr not in visited:
            visited.add(nbr)
            visit(visited, graph, nbr)

def first_time_all_connected_union_find(V, cables):
    def is_before(edge):
        graph = [[] for _ in range(V)]
        for i in range(edge + 1):
            node1, node2 = cables[i]
            graph[node1].append(node2)
            graph[node2].append(node1)
        visited = {0}
        visit(visited, graph, 0)
        return len(visited) < V
    l, r = 0, len(cables) - 1
    if is_before(r):
        return -1
    while r - l > 1:
        mid = l + (r - l) // 2
        if is_before(mid):
            l = mid
        else:
            r = mid
    return r

