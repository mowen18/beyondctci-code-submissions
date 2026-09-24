# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def max_at_most_3_bad_days(sales):
    l, r = 0, 0
    currmax = 0
    bad_days = 0
    while r < len(sales):
      can_grow = bad_days < 3 or sales[r] > 9
      if can_grow:
        if sales[r] < 10:
          bad_days += 1
        r += 1
        currmax = max(currmax, r - l)
      else:
        if sales[l] < 10:
          bad_days -= 1
        l += 1
    return currmax
