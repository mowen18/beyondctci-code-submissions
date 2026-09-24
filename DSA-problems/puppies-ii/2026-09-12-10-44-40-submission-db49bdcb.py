# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def puppy_ears(puppies):
  if puppies == 0:
    return 0
  
  if puppies % 2 == 0:
    return 3 + puppy_ears(puppies-1)
  return 2 + puppy_ears(puppies-1)
