# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def index_of(s, t):
  if not t: return 0
  if not s: return -1
  
  for i in range(len(s) - len(t) + 1):
    found = True
    for j in range(len(t)):
      if s[i + j] != t[j]:
        found = False
        break
    if found == True:
      return i
  return -1
      

