# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import heapq
def distance_in_weighted_graph(edges, V, source):
  adjlist = [[] for _ in range(V)]
  for u, v, w in edges:
    adjlist[u].append((v,w))
  
  dist = [float("inf")] * V
  dist[source] = 0
  mheap = []
  heapq.heappush(mheap, (source, 0))
  while mheap:
    node, w = heapq.heappop(mheap)
    if w > dist[node]:
      continue
    
    for nbr, weight in adjlist[node]:
      currentdist = w + weight
      if currentdist < dist[nbr]:
        dist[nbr] = currentdist
        heapq.heappush(mheap, (nbr, currentdist))
  
  res = []
  for i in range(V):
    if dist[i] == float("inf"):
      res.append(None)
    else:
      res.append(dist[i])
  return res
    
  

  

