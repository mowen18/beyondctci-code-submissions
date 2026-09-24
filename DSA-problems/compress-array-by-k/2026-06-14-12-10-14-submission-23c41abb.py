# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def compress_array_by_k(arr, k):
  stack = []

  def merge(num):
    if not stack or stack[-1][0] != num:
      stack.append([num,1])
    elif stack[-1][1] < k - 1:
      stack[-1][1] += 1
    else:
      stack.pop()
      merge(num * k)
  
  for num in arr:
    merge(num)
  
  res = []
  for num, cnt in stack:
    for _ in range(cnt):
      res.append(num)
  return res

