# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def replace_bctci(s):
  target = 'beyondcrackingthecodinginterview'
  if not s:
    return ""
  if s[0:len(target)] == target:
    return 'bctci' + replace_bctci(s[len(target):len(s)])
  
  return s[0] + replace_bctci(s[1:])
