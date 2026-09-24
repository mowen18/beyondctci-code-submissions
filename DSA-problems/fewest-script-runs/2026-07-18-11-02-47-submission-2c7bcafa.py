# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import math
def fewest_script_runs(meetings):
  meetings.sort(key=lambda x: x[1])
  cnt = 0
  prev_end = -math.inf
  for l, r in meetings:
    if prev_end < l:
      cnt += 1
      prev_end = r
  return cnt

