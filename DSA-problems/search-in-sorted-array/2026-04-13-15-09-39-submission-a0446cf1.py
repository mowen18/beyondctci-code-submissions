# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def search_in_sorted_array(arr, target):
    if len(arr) == 0:
      return -1
    l, r = 0, len(arr) - 1
    if arr[l] >= target or arr[r] <= target:
      if arr[l] == target:
        return 0
      elif arr[r] == target:
        return r
      return -1
    while r - l > 1:
      mid = (r + l) // 2
      if arr[mid] < target:
        l = mid
      else:
        r = mid
    if arr[r] == target:
      return r
    return -1
