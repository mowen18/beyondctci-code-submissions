# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def last_false_in_ascending_boolean_array(arr):
  l, r = 0, len(arr)
  if not arr: return -1
  while l < r:
    mid = (l + r) // 2
    if arr[mid] == True:
      r = mid
    else:
      l = mid + 1
  if arr[l-1] == False:
    return l-1
  return -1
