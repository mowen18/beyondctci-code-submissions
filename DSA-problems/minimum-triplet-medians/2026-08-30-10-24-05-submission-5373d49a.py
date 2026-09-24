# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def minimum_triplet_medians(arr):
  arr.sort()
  med_sum = 0
  for i in range(len(arr) // 3):
    med_sum += arr[i * 2 + 1]
  return med_sum
