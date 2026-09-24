# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def search_in_sorted_array(arr, target):
  if len(arr) < 1:
    return -1
  l, r = 0, len(arr) - 1
  if arr[l] == target:
    return l
  if arr[r] == target:
    return r

  while r - l > 1:
    mid = l + (r - l) // 2
    if arr[mid] < target:
      l = mid
    else:
      r = mid
  if arr[r] != target:
    return -1
  return r

