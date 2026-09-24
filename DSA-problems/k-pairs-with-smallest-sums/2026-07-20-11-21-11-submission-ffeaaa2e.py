# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import heapq
def k_pairs_with_smallest_sums(arr1, arr2, k):
  if not arr1 or not arr2:
    return []
  min_heap = [(arr1[0] + arr2[0], arr1[0], 0, 0)]
  res = []
  seen = {(0,0)}
  while min_heap and len(res) < k:
    _, _, i, j = heapq.heappop(min_heap)
    res.append([arr1[i],arr2[j]])
    if i + 1 < len(arr1) and (i + 1, j) not in seen:
      heapq.heappush(min_heap, (arr1[i + 1] + arr2[j], arr1[i + 1], i + 1, j))
      seen.add((i+1, j))
    if j + 1 < len(arr2) and (i, j + 1) not in seen:
      heapq.heappush(min_heap, (arr1[i] + arr2[j+1], arr1[i], i, j + 1))
      seen.add((i, j+1))
  
  return res

