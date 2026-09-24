# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def balance_point(arr):
    prefix_sum = []
    prefix_sum.append(arr[0])
    for i in range(1, len(arr)):
      prefix_sum.append(prefix_sum[i-1] + arr[i])
    post_fix_sum = [0] * len(arr)
    post_fix_sum[-1] = arr[-1]
    for i in range(len(arr)-2, -1,-1):
      post_fix_sum[i] = post_fix_sum[i + 1] + arr[i]
    for i in range(len(prefix_sum)):
      if prefix_sum[i] == post_fix_sum[i]:
        return i
    return -1

