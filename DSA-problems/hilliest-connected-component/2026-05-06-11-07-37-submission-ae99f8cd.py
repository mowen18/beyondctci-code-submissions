# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def hilliest_connected_component(graph, heights):
    node_to_cc = {}

    def visit(node, cc):
      if node in node_to_cc:
        return
      node_to_cc[node] = cc
      for nbr in graph[node]:
        visit(nbr, cc)
    
    def get_cc(graph):
      cc = 0
      for node in range(len(graph)):
        if node not in node_to_cc:
          visit(node, cc)
          cc += 1
      return node_to_cc
    
    nodecc = get_cc(graph)
    cc_count = {}
    cc_sum_height = {}
    for node in range(len(graph)):
      cc = nodecc[node]
      if cc not in cc_count:
        cc_count[cc] = 0
        cc_sum_height[cc] = 0
      for nbr in graph[node]:
        if nbr > node:
          cc_count[cc] += 1
          cc_sum_height[cc] += abs(heights[node] - heights[nbr])
    res = 0
    for cc in cc_count:
      if cc_count[cc] > 0:
        res = max(res, cc_sum_height[cc] / cc_count[cc])
    return res
      


    

    

