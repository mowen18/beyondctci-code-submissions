# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def intersection(interval1, interval2):
  x = max(interval1[0], interval2[0])
  y = min (interval1[1], interval2[1])
  return [x, y]

def interval_intersection(arr1, arr2):
  p1, p2 = 0, 0
  res = []
  while p1 < len(arr1) and p2 < len(arr2):
    int1, int2 = arr1[p1], arr2[p2]
    if int1[1] < int2[0]:
      p1 += 1
    elif int2[1] < int1[0]:
      p2 += 1
    else:
      res.append(intersection(int1, int2))
      if int1[1] < int2[1]:
        p1 += 1
      else:
        p2 += 1
  return res

    
