# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def find_through_api(target, fetch):
  
  def is_before(index):
    return fetch(index) != -1 and fetch(index) < target

  r = 1
  while is_before(r):
    r *= 2
  if fetch(0) == target:
    return 0
  l = 0
  while r - l > 1:
    mid = (l + r) // 2
    if is_before(mid):
      l = mid
    else:
      r = mid
  if fetch(r) == target:
    return r
  return -1
