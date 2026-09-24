# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import heapq
def first_k(arr, k):
  heap = []
  for num in arr:
    heapq.heappush_max(heap, num)
    if len(heap) > k:
      heapq.heappop_max(heap)
  
  return [x for x in heap]

  
