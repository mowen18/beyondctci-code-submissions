# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def count_subarrays_with_bad_days_in_range(sales, k1, k2):
  
  def at_most(sales, k):
    l, r = 0, 0
    window_bad = 0
    cnt = 0
    while r < len(sales):
      can_grow = sales[r] >= 10 or window_bad < k
      if can_grow:
        if sales[r] < 10:
          window_bad += 1
        r += 1
        cnt += r - l
      else:
        if sales[l] < 10:
          window_bad -= 1
        l += 1
    return cnt
  
  if k1 == 0:
    return at_most(sales, k2)
  return at_most(sales, k2) - at_most(sales, k1 -1)
  


