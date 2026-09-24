# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def longest_subarray_with_sum_k(arr, k):
  prefix_sum = [0] * len(arr)
  prefix_sum[0] = arr[0]
  for i in range(1, len(arr)):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]
  prefix_sum_index = {0: -1}
  res = -1
  for r, val in enumerate(prefix_sum):
    if val - k in prefix_sum_index:
      l = prefix_sum_index[val - k]
      res = max(res, r - l)
    if val not in prefix_sum_index:
      prefix_sum_index[val] = r
  return res

