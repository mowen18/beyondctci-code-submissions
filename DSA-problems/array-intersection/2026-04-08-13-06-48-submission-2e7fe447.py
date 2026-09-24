# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def common_elements(arr1, arr2):
    p1, p2 = 0, 0
    res = []
    while p1 < len(arr1) and p2 < len(arr2):
      if arr1[p1] == arr2[p2]:
        res.append(arr1[p1])
        p1 += 1
        p2 += 1
      elif arr1[p1] < arr2[p2]:
        p1 += 1
      else:
        p2 += 1
    return res

