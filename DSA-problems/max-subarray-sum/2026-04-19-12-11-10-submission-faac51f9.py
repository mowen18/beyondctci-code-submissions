# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def max_subarray_sum(arr):
    if max(arr) < 0:
      return max(arr)
    r = 0
    maxsum = 0
    currwin = 0
    while r < len(arr):
      can_grow = currwin + arr[r] >= 0
      if can_grow:
        currwin += arr[r]
        r += 1
        maxsum = max(maxsum, currwin)
      else:
        currwin = 0
        r += 1
    return maxsum
