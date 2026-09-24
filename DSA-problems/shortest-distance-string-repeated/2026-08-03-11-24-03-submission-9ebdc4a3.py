# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import math
def shortest_distance_string_repeated(words):
  last_seen = {}
  mindist = math.inf
  for i, word in enumerate(words):
    if word in last_seen:
      diff = i - last_seen[word]
      mindist = min(mindist, diff)
    last_seen[word] = i
  if mindist == math.inf: return -1
  return mindist
