# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import heapq, math

def edge_in_mst(v, edges, i):
  def build_list(edges, v, iskip = None):
    adj = [[] for _ in range(v)]
    for idx, (n1, n2, w) in enumerate(edges):
      if iskip is not None and idx == iskip:
        continue
      adj[n1].append((n2, w))
      adj[n2].append((n1, w))
    return adj

  def prim(v, edges, skip = None):
    adjlist = build_list(edges, v, skip)
    min_edge = [math.inf for _ in range(v)]
    mst_cost = 0
    min_edge[0] = 0
    heap = [(0, 0)]
    vis = [False for _ in range(v)]
    while heap:
      w, node = heapq.heappop(heap)

      if vis[node]:
        continue
      vis[node] = True
      mst_cost += min_edge[node]

      for u, w in adjlist[node]:
        if not vis[u] and w < min_edge[u]:
          min_edge[u] = w
          heapq.heappush(heap, (w, u))
    if not all(vis): return math.inf
    return mst_cost

  return prim(v, edges, i) > prim(v, edges)
