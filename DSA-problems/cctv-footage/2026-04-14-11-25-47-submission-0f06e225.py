# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def cctv_footage(t1, t2, is_stolen):
    l, r = t1, t2
    while r - l > 1:
      mid = (l + r) // 2
      if not is_stolen(mid):
        l = mid
      else:
        r = mid
    return r
      

