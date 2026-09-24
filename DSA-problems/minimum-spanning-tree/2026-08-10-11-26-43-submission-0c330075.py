# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import heapq, math
def minimum_spanning_tree(v, edges):
  adj = [[] for _ in range(v)]
  for n1, n2, w in edges:
    adj[n1].append((n2, w))
    adj[n2].append((n1, w))
  
  def prim():
    min_edge = [math.inf for _ in range(v)]
    mst_cost = 0
    min_edge[0] = 0
    heap = [(0,0)]
    vis = [False for _ in range(v)]
    while heap:
      w, node = heapq.heappop(heap)

      if vis[node]:
        continue
      vis[node] = True
      mst_cost += min_edge[node]
      
      for u, w in adj[node]:
        if not vis[u] and w < min_edge[u]:
          min_edge[u] = w
          heapq.heappush(heap, (w, u))
    return mst_cost
  
  return prim()
      




