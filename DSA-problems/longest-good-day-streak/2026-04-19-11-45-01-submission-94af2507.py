# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def max_no_bad_days(sales):
    l, r = 0, 0
    currmax = 0
    maxdays = 0
    while r < len(sales):
      can_grow = l == r or sales[l] > 9 and sales[r] > 9
      if can_grow:
        if sales[r] > 9:
          currmax += 1
        r += 1
        maxdays = max(maxdays, currmax)
      else:
        l = r
        currmax = 0
    return maxdays
