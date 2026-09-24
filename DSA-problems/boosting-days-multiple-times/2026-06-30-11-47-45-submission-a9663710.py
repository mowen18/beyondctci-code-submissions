# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def max_consecutive_with_k_boosts(projected_sales, k):
  l, r = 0, 0
  curmax = 0
  curboosts = 0
  while r < len(projected_sales):
    can_grow = curboosts + max(10-projected_sales[r], 0) <= k
    if can_grow:
      curboosts += max(10-projected_sales[r],0)
      r += 1
      curmax = max(curmax, r - l)
    elif r==l:
      r += 1
      l += 1
    else:
      curboosts -= max(10-projected_sales[l], 0)
      l += 1
  return curmax

