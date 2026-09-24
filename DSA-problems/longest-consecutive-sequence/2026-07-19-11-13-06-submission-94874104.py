# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def longest_consecutive_sequence(arr):
  s = set(arr)
  maxcnt = 0
  for num in arr:
    if num - 1 not in s:
      curr = num
      cnt = 1
      while curr + 1 in s:
        curr = curr + 1
        cnt += 1
      maxcnt = max(maxcnt, cnt)
  return maxcnt
  
    

