# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def three_sum(arr, w):
  dic = {}
  for i in range(len(arr)):
    if arr[i] not in dic:
      dic[arr[i]] = []
    dic[arr[i]].append(i)
  
  for i in range(len(arr)-1):
    for j in range(i + 1, len(arr)):
      target = w - arr[i] - arr[j]
      if target in dic:
        for k in dic[target]:
          if k > j:
            return True
  return False
