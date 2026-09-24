# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def all_star(s):
  if len(s) <= 1:
    return s
    
  return s[0] + "*" + all_star(s[1:])


