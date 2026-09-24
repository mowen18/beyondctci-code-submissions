# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def blocks(n):
  if n == 1:
    return 1
  
  def roof(n):
    if n == 1:
      return 1
    
    return 2 * roof(n-1) + 1
  
  return blocks(n-1) * 4 + roof(n) ** 2
