# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def delay_memoized(times):
  n = len(times)
  if n < 3:
    return 0
  memo = {}
  def delay_rec(stop):
    if stop >= n - 3:
      return times[stop]
    if stop in memo:
      return memo[stop]
    memo[stop] = times[stop] + min(delay_rec(stop + 1), delay_rec(stop + 2), delay_rec(stop + 3))
    return memo[stop]
  return min(delay_rec(0), delay_rec(1), delay_rec(2))
