# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def sanitize(s):
  
  if len(s) <= 1:
    return s
  
  if s[0] != s[1]:
    return s[0] + sanitize(s[1:])
  return sanitize(s[1:])
  

