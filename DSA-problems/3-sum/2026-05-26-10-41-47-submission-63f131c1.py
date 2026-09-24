# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def three_sum(arr, w):
  if len(arr) < 3:
    return False
  sarr = sorted(arr)

  for i in range(len(sarr)-2):
    l = i + 1
    r = len(sarr) - 1

    while l < r:
      if sarr[i] + sarr[l] + sarr[r] == w:
        return True
      elif sarr[i] + sarr[l] + sarr[r] < w:
        l += 1
      else:
        r -= 1
  return False
