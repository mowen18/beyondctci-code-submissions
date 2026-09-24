# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import heapq
def diminish_largest(arr, k):
  if len(arr) < 1:
    return 0
  heapq.heapify_max(arr)
  for _ in range(k):
    num = heapq.heappop_max(arr)
    num = (num // 2)
    heapq.heappush_max(arr, num)
  return sum(arr)
