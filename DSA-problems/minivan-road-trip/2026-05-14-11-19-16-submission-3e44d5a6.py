# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import math
def minivan_road_trip(times, k):
  memo ={}
  n = len(times)
  def delay_rec(stop, k):
    future_min = math.inf
    if len(times) <= k:
      return 0
    if stop >= n - k - 1:
      return times[stop]
    if stop in memo:
      return memo[stop]
    for i in range(1, k + 2):
      candidate = times[stop] + delay_rec(stop + i, k)
      future_min = min(future_min, candidate)
    memo[stop] = future_min
    return memo[stop]
  future_min = math.inf
  res = []
  for i in range(0, k + 1):
    res.append(delay_rec(i, k))
  return min(res)

    
    



