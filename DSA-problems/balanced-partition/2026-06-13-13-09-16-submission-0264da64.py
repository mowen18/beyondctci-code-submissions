# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def max_balanced_partition(s):

  height = 0
  res = 0
  for char in s:
    if char == '(':
      height += 1
    if char == ')':
      height -= 1
    if height == 0:
      res += 1
  return res

  
