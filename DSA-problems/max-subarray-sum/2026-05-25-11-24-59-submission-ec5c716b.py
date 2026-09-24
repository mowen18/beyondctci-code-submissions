# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import math
def max_subarray_sum(arr):
  r = 0
  cur_sum = 0
  max_sum = -math.inf
  if max(arr) < 0:
    return max(arr)
  while r < len(arr):
    if (cur_sum + arr[r]) >= 0:
      cur_sum += arr[r]
      r += 1
      max_sum = max(max_sum, cur_sum)
    else:
      cur_sum = 0
      r += 1
  return max_sum

