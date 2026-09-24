# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def time_traveler(jumping_points, k, max_aging):
  gaps = []
  n = len(jumping_points)
  for i in range(1, len(jumping_points)):
    gaps.append(jumping_points[i] - jumping_points[i-1])
  gaps.sort()
  total_aging = sum(gaps[:n - 1 -k])
  return max_aging >= total_aging
