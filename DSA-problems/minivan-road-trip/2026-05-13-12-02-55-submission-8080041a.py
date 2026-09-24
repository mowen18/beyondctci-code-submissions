# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import math
def minivan_road_trip(times, k):
  if len(times) <= k:
    return 0
  
  memo = {}
  
  def times_rec(stop):
    min_future = math.inf
    if stop >= len(times) - k - 1:
      return times[stop]
    if stop in memo:
      return memo[stop]
    for i in range(1, k + 2):
      candidate_delay = times_rec(stop + i)
      min_future = min(min_future, candidate_delay)
    memo[stop] = times[stop] + min_future
    return memo[stop]
  min_delay = math.inf
  for stop in range(k + 1):
    candidate_delay = times_rec(stop)
    min_delay = min(min_delay, candidate_delay)
  return min_delay

  
