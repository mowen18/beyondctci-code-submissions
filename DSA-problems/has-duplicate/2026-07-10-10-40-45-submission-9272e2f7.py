# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def has_duplicate(arr):
  s = set()
  for i in arr:
    if i in s:
      return True
    s.add(i)
  return False
