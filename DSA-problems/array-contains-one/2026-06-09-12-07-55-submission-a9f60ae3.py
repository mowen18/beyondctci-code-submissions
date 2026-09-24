# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def array_contains_one(arr):
  if not arr:
    return False
  arr.sort()
  def rec(n):
    if arr[n] == 1:
      return True
    if n == len(arr) - 1:
      return False
    return rec(n+1)
  return rec(0)

