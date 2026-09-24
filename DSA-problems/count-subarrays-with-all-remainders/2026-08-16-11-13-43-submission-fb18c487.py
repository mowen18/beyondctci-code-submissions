# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def at_most_two(arr):
  window_count = {}
  count = 0
  r, l = 0, 0
  while r < len(arr):
    can_grow = arr[r] % 3 in window_count or len(window_count) < 2
    if can_grow:
      if arr[r] % 3 not in window_count:
        window_count[arr[r] % 3] = 0
      window_count[arr[r] % 3] += 1
      r += 1
      count += r - l
    else:
      window_count[arr[l] % 3] -= 1
      if window_count[arr[l] % 3] == 0:
        del window_count[arr[l] % 3]
      l += 1
  return count

def count_subarrays_with_all_remainders(arr):
  n = len(arr)
  cnt = n * (n + 1) // 2
  return cnt - at_most_two(arr)
  

