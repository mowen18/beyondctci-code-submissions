# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def max_consecutive_good_days(projected_sales, k):

  l, r = 0, 0
  boostlim = 0
  maxdays = 0
  while r < len(projected_sales):
    can_grow = projected_sales[r] >= 10 or boostlim < k
    if can_grow:
      if projected_sales[r] < 10:
        boostlim += 1
      r += 1
      maxdays = max(maxdays, r - l)
    else:
      if projected_sales[l] < 10:
        boostlim -= 1
      l += 1
  return maxdays

  


