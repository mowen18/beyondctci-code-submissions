# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import math
def shortest_period_with_over_20_sales(sales):
  l, r = 0, 0
  mindays = math.inf
  cursum = 0
  while True:
    can_grow = cursum <= 20
    if can_grow:
      if r == len(sales):
        break
      cursum += sales[r]
      r += 1
    else:
      mindays = min(mindays, r - l)
      cursum -= sales[l]
      l += 1
  if mindays == math.inf:
    return -1
  return mindays
        



