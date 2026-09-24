# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def last_true(arr):
  if not arr: return -1
  l , r = 0, len(arr)

  while l < r:
    mid = (l + r) // 2
    if arr[mid] == False:
      r = mid
    else:
      l = mid + 1
  if arr[l-1] == True:
    return l - 1
  return -1
  