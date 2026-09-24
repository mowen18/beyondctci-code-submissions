# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def max_subarray_sum(arr):
  if max(arr) < 0:
    return max(arr)
  max_sum = arr[0]
  r = 0
  cursum = 0
  while r < len(arr):
    can_grow = arr[r] + cursum >= 0
    if can_grow:
      cursum += arr[r]
      r += 1
      max_sum = max(max_sum, cursum)
    else:
      cursum = 0
      r += 1
  return max_sum


