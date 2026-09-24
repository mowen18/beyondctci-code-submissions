# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def most_ones_with_k_flips(arr, k):
  l, r = 0, 0
  count = 0
  flips = 0
  while r < len(arr):
    can_grow = arr[r] == 1 or flips < k
    if can_grow:
      if arr[r] == 0:
        flips += 1
      r += 1
      count = max(count, r - l)
    else:
      if arr[l] == 0:
        flips -= 1
      l += 1
  return count

