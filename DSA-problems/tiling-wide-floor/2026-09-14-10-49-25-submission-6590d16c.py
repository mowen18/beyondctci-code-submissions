# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def tilings(n):
  
  memo = {}
  def rec(tiles):
    if tiles <= 2:
      return 1
    if tiles in memo:
      return memo[tiles]
    
    memo[tiles] = rec(tiles-1) + rec(tiles-3)
    return memo[tiles]
  
  return rec(n)
