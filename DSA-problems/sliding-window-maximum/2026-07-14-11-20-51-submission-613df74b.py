# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import math
from collections import deque
def sliding_window_max(arr, k):

  candidates = deque()
  res = []
  for i, num in enumerate(arr):

    if candidates and candidates[0] < i - k + 1:
      candidates.popleft()
    

    while candidates and arr[candidates[-1]] <= num:
      candidates.pop()

    candidates.append(i)

    if i >= k - 1:
      res.append(arr[candidates[0]])
  return res

      




