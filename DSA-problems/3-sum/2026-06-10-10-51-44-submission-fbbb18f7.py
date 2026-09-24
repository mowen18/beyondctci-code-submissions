# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def three_sum(arr, w):
  arr.sort()


  for i in range(len(arr)-2):
    l = i + 1
    r = len(arr) - 1
    while l < r:
      val = arr[i] + arr[l] + arr[r]
      if val < w:
        l += 1
      elif val > w:
        r -= 1
      else:
        return True 
  return False

