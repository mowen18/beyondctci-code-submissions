# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import math
def dag_distances(graph, start):
    def topo(graph):
        V = len(graph)
        degree_zero = []
        in_degree = [0 for _ in range(V)]
        for node in range(V):
            for nbr, _ in graph[node]:
                in_degree[nbr] += 1
        
        for node in range(V):
            if in_degree[node] == 0:
                degree_zero.append(node)
        topo_order = []
        while degree_zero:
            node = degree_zero.pop()
            topo_order.append(node)
            for nbr, _ in graph[node]:
                in_degree[nbr] -= 1
                if in_degree[nbr] == 0:
                    degree_zero.append(nbr)
        if len(topo_order) < V:
            return []
        return topo_order
    
    
    toporder = topo(graph)
    distances = {start: 0}
    for node in toporder:
        if node not in distances:
            continue
        for nbr, weight in graph[node]:
            if nbr not in distances or distances[node] + weight < distances[nbr]:
                distances[nbr] = distances[node] + weight
    res = []
    for i in range(len(graph)):
        if i not in distances:
            res.append(None)
        else:
            res.append(distances[i])
    return res

