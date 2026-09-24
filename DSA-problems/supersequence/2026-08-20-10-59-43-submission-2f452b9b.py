# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def supersequence(arr):
    def top_sort(graph):
        in_degree = {}
        for node in graph:
            in_degree[node] = 0
        for node in graph:
            for nbr in graph[node]:
                in_degree[nbr] += 1
        deg_zero = []
        for node in in_degree:
            if in_degree[node] == 0:
                deg_zero.append(node)
        top_order = []
        while deg_zero:
            node = deg_zero.pop()
            top_order.append(node)
            for nbr in graph[node]:
                in_degree[nbr] -= 1
                if in_degree[nbr] == 0:
                    deg_zero.append(nbr)
        return len(top_order) == len(graph)
    
    graph = {}
    for word in arr:
        for c in word:
                graph[c] = set()
    
    for word in arr:
        for i in range(len(word)-1):
            graph[word[i]].add(word[i + 1])
    return top_sort(graph)
    

        
    

