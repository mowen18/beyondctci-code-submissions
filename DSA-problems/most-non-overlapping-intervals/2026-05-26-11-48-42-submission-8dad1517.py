# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import math
def most_non_overlapping_intervals(intervals):
  intervalss = sorted(intervals, key = lambda x: x[1])
  count = 0
  prev = -math.inf
  for l, r in intervalss:
    if l > prev:
      count += 1
      prev = r
  return count

