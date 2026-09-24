# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def strongly_connected(graph):
    V = len(graph)
   
    def visit(node, graph2, visited):
        if node in visited:
            return
        visited.add(node)
        for nbr in graph2[node]:
            visit(nbr, graph2, visited)
    visiteds = set()
    visit(0, graph, visiteds)
    if len(visiteds) != V:
        return False
           
    adj_l_reversed = [[] for _ in range(V)]
    for node1 in range(V):
        for node2 in graph[node1]:
            adj_l_reversed[node2].append(node1)
    visitedrev = set()
    visit(0, adj_l_reversed, visitedrev)
    return len(visitedrev) == V



    

        
        
