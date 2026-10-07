# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def interval_xor(a, b):
  if a[0] > b[0]:
    return interval_xor(b, a)
  
  a_s, a_e = a
  b_s, b_e = b

  if a_s < b_s:

    if a_e < b_s:
      return [[a_s, a_e], [b_s, b_e]]
    
    if a_e == b_s:
      return [[a_s, b_e]]
    if a_e < b_e:
      return [[a_s, b_s], [a_e, b_e]]
    
    if a_e == b_e:
      return [[a_s, b_s]]
    if a_e > b_e:
      return [[a_s, b_s], [b_e, a_e]]
  if a_s == b_s:
    if a_e < b_e:
      return [[a_e, b_e]]
    if a_e == b_e:
      return []
    if a_e > b_e:
      return [[b_e, a_e]]
