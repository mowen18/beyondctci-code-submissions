# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def count_subarrays_with_exactly_k_bad_days(sales, k):
  def at_most(k):
    l, r = 0, 0
    windowcnt = 0
    count = 0
    while r < len(sales):
      can_grow = sales[r] >= 10 or windowcnt < k
      if can_grow:
        if sales[r] < 10:
          windowcnt += 1
        r += 1
        count += r - l
      else:
        if sales[l] < 10:
          windowcnt -= 1
        l += 1
    return count
  if k == 0: return at_most(k)
  return at_most(k) - at_most(k-1)
  
