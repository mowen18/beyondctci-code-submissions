# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import math
def min_pages_per_day(page_counts, days):
  
  def num_days(daily_lim):
    days = 0
    for pages in page_counts:
      days += math.ceil(pages / daily_lim)
    
    return days
  
  def is_before(daily_lim):
    return num_days(daily_lim) > days
  l, r = 0, max(page_counts)
  while r - l > 1:
    mid = l + (r - l) // 2
    if is_before(mid):
      l = mid
    else:
      r = mid
  return r
