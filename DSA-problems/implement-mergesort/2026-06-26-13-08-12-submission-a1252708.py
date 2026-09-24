# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def mergesort(arr):
  if len(arr) <= 1:
    return arr
  mid = len(arr) // 2
  left = mergesort(arr[:mid])
  right = mergesort(arr[mid:])
  return merge(left, right)

def merge(left, right):
  l = 0
  r = 0
  res = []
  while l < len(left) and r < len(right):
    if left[l] <= right[r]:
      res.append(left[l])
      l += 1
    else:
      res.append(right[r])
      r += 1
  
  res.extend(left[l:])
  res.extend(right[r:])
  return res


