# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import math
def find_all_squares(arr):
  mp = {}
  res = []
  for i, j in enumerate(arr):
    mp[j] = i
  for i in range(len(arr)):
    num = arr[i] ** 2
    if num in mp:
      res.append([i, mp[num]])
  return res
  


  

