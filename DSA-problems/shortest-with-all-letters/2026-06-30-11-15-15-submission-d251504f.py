# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
from collections import defaultdict
import math
def shortest_with_all_letters(s1, s2):
  l, r = 0, 0
  missing = defaultdict(int)
  for c in s2:
    missing[c] += 1
  current_missing = len(missing)
  curmin = math.inf
  while True:
    if current_missing > 0:
      if r >= len(s1):
        break
      if s1[r] in missing:
        missing[s1[r]] -= 1
        if missing[s1[r]] == 0:
          current_missing -= 1
      r += 1
    else:
      curmin = min(curmin, r - l)
      if s1[l] in missing:
        missing[s1[l]] += 1
        if missing[s1[l]] == 1:
          current_missing += 1
      l += 1
  if curmin >= len(s2) and curmin != math.inf:
    return curmin
  return -1






