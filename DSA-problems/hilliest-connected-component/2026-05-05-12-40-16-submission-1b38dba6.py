# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def connected_cc(graph):
    node_to_cc = {}
    def visit(node, cc):
        if node in node_to_cc:
            return
        node_to_cc[node] = cc
        for nbr in graph[node]:
            visit(nbr, cc)
    cc_id = 0
    for node in range(len(graph)):
        if node not in node_to_cc:
            visit(node, cc_id)
            cc_id += 1
    return node_to_cc

def hilliest_connected_component(graph, heights):
    node_to_cc = connected_cc(graph)
    cc_elevation_sum = {}
    cc_count = {}
    for node in range(len(graph)):
        cc = node_to_cc[node]
        if cc not in cc_elevation_sum:
            cc_elevation_sum[cc] = 0
            cc_count[cc] = 0
        for nbr in graph[node]:
            if nbr > node:
                cc_count[cc] += 1
                cc_elevation_sum[cc] += abs(heights[node] - heights[nbr])
    res = 0
    for cc in cc_count:
        if cc_count[cc] > 0:
            res = max(res, cc_elevation_sum[cc] / cc_count[cc])
    return res

