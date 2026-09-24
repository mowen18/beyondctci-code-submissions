# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def balance_point(arr):
  prefix_sums = []
  n = len(arr)
  if not arr:
    return -1
  prefix_sums.append(arr[0])
  for i in range(1, n):
    prefix_sums.append(prefix_sums[i-1] + arr[i])
  postfix_sums = [0] * n
  postfix_sums[n-1] = arr[n-1]
  for i in range(n-2, -1, -1):
    postfix_sums[i] = postfix_sums[i + 1] + arr[i]
  for i in range(n):
    if postfix_sums[i] == prefix_sums[i]:
      return i
  return -1   