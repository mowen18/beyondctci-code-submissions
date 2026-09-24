# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def puppy_ears(puppies):
  
  if puppies == 0:
    return 0
  
  return 2 + puppy_ears(puppies - 1)
