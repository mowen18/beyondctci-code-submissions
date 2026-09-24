# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import heapq
def k_smallest_elements(heap, k):
  if not heap: return []
  candidates = []
  heapq.heappush(candidates, (heap[0], 0))
  res = []
  for _ in range(k):

    if not candidates:
      break
    
    num, idx = heapq.heappop(candidates)

    res.append(num)

    left = 2 * idx + 1
    right = 2 * idx + 2

    if left < len(heap):
      heapq.heappush(candidates, (heap[left], left))
    if right < len(heap):
      heapq.heappush(candidates, (heap[right], right))
  return res

