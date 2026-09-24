# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def most_weekly_sales(sales):
  l, r = 0, 0
  max_sales = 0
  window_sum = 0
  while r < len(sales):
    window_sum += sales[r]
    r += 1
    if r - l == 7:
      max_sales = max(max_sales, window_sum)
      window_sum -= sales[l]
      l += 1
  return max_sales
    

