# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def most_weekly_sales(sales):
  if len(sales) < 7: return 0
  l, r = 0, 0
  cur_best = 0
  curwindow = 0
  while r < len(sales):
    if r - l < 6:
      r += 1
      cur_best = max(cur_best, sum(sales[l:r + 1]))
    else:
      l += 1
  return cur_best
      



