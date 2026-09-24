# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def merge(arr1, arr2):
  p1, p2 = 0, 0
  res = []

  while p1 < len(arr1) and p2 < len(arr2):
    if arr1[p1] <= arr2[p2]:
      res.append(arr1[p1])
      p1 += 1
    elif arr1[p1] >= arr2[p2]:
      res.append(arr2[p2])
      p2 += 1
  while p1 < len(arr1):
    res.append(arr1[p1])
    p1 += 1
  while p2 < len(arr2):
    res.append(arr2[p2])
    p2 += 1
  return res
    
    
    


