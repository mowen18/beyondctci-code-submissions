# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def max_at_most_3_bad_days(sales):
    l, r = 0,0
    curmax = 0
    num_bad = 0
    if not sales:
      return 0
    while r < len(sales):
      can_grow = sales[r] > 9 or num_bad < 3
      if can_grow:
        if sales[r] < 10:
          num_bad += 1
        r += 1
        curmax = max(curmax, r - l)
      elif not can_grow and sales[l] < 10:
        l += 1
        num_bad -=1
      else:
        l += 1
    return curmax



