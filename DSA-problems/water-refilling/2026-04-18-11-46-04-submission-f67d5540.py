# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def num_refills(a, b):
    def is_before(num_pours):
      return num_pours * b <= a
    
    kpours = 1
    while is_before(kpours * 2):
      kpours *= 2
    
    l, r = kpours, kpours * 2
    while r - l > 1:
      mid = (r + l) >> 1
      if is_before(mid):
        l = mid
      else:
        r = mid
    return l
