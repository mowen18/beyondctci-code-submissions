# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def latest_reachable_year(jumping_points, k, max_aging):
  n = len(jumping_points)

  def gap_size(year_idx):
    return jumping_points[year_idx + 1] - jumping_points[year_idx]
  
  sorted_gaps = sorted(range(n-1), key=gap_size, reverse=True)

  def year_reached(gaps_skipped):
    return jumping_points[0] + max_aging + sum(gap_size(i) for i in gaps_skipped)
  
  def can_reach(year_idx):
    jumps_used = 0
    total_aging = 0
    for idx in sorted_gaps:
      if idx >= year_idx:
        continue
      if jumps_used < k:
        jumps_used += 1
      else:
        total_aging += gap_size(idx)
        if total_aging > max_aging:
          return False
    return True

  l, r = 0, n - 1
  if can_reach(r):
    return year_reached(sorted_gaps[:k])

  while r - l > 1:
    mid = (r + l) // 2
    if can_reach(mid):
      l = mid
    else:
      r = mid
  
  gaps_to_l = sorted(range(l), key=gap_size, reverse = True)
  return year_reached(gaps_to_l[:k])




