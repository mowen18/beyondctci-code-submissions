# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import math
def nearest_repeated_distance(numbers):
  last_seen = {}
  mindist = math.inf
  for idx, num in enumerate(numbers):
    if num in last_seen:
      diff = idx - last_seen[num]
      mindist = min(mindist, diff)
    last_seen[num] = idx

  if mindist == math.inf: return -1
  return mindist
  
