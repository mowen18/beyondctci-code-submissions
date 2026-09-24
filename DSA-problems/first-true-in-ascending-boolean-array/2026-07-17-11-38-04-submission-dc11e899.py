# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def first_true(arr):
  if len(arr) < 1: return -1
  lo, hi = 0, len(arr)
  def is_mid(index):
    if arr[index] == True:
      return True
    return False
  
  while lo < hi:
    mid = (lo + hi) // 2
    if arr[mid] == True:
      hi = mid
    else:
      lo = mid + 1
  if lo < len(arr):
    return lo
  return -1
  
