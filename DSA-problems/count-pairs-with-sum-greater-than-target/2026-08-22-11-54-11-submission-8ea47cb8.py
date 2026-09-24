# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def count_pairs(arr, target):
  l, r = 0, len(arr) - 1
  cnt = 0
  while l < r:
    if arr[l] + arr[r] >= target:
      cnt += r - l
      r -= 1
    else:
      l += 1
  return cnt
