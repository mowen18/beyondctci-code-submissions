# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import math
def max_laminal_sum(arr):
  best = -math.inf
  def rec(l, r):
    if r - l == 1:
      return arr[l]
    mid = (l + r) // 2
    option1 = rec(l, mid)
    option2 = rec(mid, r)
    option3 = sum(arr[l:r])
    return max(option1, option2, option3)
  return rec(0, len(arr))


