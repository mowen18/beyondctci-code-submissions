# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def lego_castle(n):
  
  if n == 1:
    return 1
    
  
  def roof(num):
    if num == 1:
      return 1
    
    return roof(num - 1) * 2 + 1
  
  return lego_castle(n - 1) * 2 + roof(n)
  

