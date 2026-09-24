# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def connected_component_queries(graph, queries):
    def visit(node, cc_id):
      if node in node_to_cc:
        return
      node_to_cc[node] = cc_id
      for nbr in graph[node]:
        visit(nbr, cc_id)

#ccq(graph, querues):
    node_to_cc = {}
    cc_id = 0
    res = []
    for node in range(len(graph)):
      if node not in node_to_cc:
        visit(node, cc_id)
        cc_id += 1

    for node1, node2 in queries:
      res.append(node_to_cc[node1] == node_to_cc[node2])
    return res
    
      
