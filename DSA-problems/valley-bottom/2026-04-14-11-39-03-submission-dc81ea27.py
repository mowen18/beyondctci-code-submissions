# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def valley_bottom(arr):
    l, r = 0, len(arr) - 1
    while r - l > 1:
      mid = (l + r) // 2
      if arr[mid] > arr[l]:
        r = mid
      else:
        l = mid
    if arr[l] < arr[r]:
      return arr[l]
    return arr[r]
