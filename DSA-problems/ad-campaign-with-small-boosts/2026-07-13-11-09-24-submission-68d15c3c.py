# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def max_consecutive_good_days_with_small_boost(projected_sales, k):
  l, r = 0, 0
  boosts = 0
  max_good_days = 0
  while r < len(projected_sales):
    can_grow = (boosts < k and 5 <= projected_sales[r] < 10) or projected_sales[r] >= 10
    if can_grow:
      if projected_sales[r] < 10:
        boosts += 1
      r += 1
      max_good_days = max(max_good_days, r - l)
    elif l == r:
      l += 1
      r += 1
    else:
      if 10 - k <= projected_sales[l] < 10:
        boosts -= 1
      l += 1
  return max_good_days
