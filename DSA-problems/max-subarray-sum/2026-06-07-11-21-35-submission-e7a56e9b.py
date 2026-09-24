# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import math
def max_subarray_sum(arr):
  cursum = 0
  maxsum = -math.inf
  #maxsum = arr[0]
  for n in arr:
    cursum = max(cursum, 0)
    cursum += n
    maxsum = max(maxsum, cursum)
  return maxsum


