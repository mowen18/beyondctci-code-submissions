# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
from collections import deque
def largest_temperature_change(arr, k):
  max_q = deque()
  min_q = deque()
  max_diff = 0
  for i, temp in enumerate(arr):
    window = i - k + 1

    if max_q and max_q[0] < window:
      max_q.popleft()
    if min_q and min_q[0] < window:
      min_q.popleft()
    
    while max_q and arr[max_q[-1]] <= arr[i]:
      max_q.pop()
    while min_q and arr[min_q[-1]] >= arr[i]:
      min_q.pop()

    max_q.append(i)
    min_q.append(i)

    if i >= k - 1:
      max_diff = max(max_diff, arr[max_q[0]]-arr[min_q[0]])

  return max_diff





