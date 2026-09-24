# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def smallest_range_with_k_elements(arr, k):
  arr.sort()
  l, r = 0, 0
  low, high = 0, float('inf')
  while True:
    must_grow = (r - l) < k
    if must_grow:
      r += 1
      if r > len(arr):
        break
    else:
      if arr[r - 1] - arr[l] < high - low:
        low = arr[l]
        high = arr[r-1]
      l += 1
  return [low, high]



