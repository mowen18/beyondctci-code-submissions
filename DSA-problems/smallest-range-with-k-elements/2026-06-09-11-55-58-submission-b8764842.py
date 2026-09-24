# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def smallest_range_with_k_elements(arr, k):
  arr.sort()
  l, r = 0, 0
  low, high = 0, float('inf')
  while r < len(arr):
    must_grow = (r - l) < k - 1
    if must_grow:
      r += 1
      #if r > len(arr):
        #break
    else:
      if arr[r] - arr[l] < high - low:
        low = arr[l]
        high = arr[r]
      l += 1
  return [low, high]



