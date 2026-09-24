# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def power_up(base, n):
  if n == 0:
    return 1
  
  return base * power_up(base, n-1)
