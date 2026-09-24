# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def first_non_negative(arr):
  if not arr: return -1
  l, r = 0, len(arr)

  while l < r:
    mid = (l + r) // 2
    if arr[mid] >= 0:
      r = mid
    else:
      l = mid + 1
  
  if l >= len(arr) or arr[l] < 0:
    return -1
  return l
