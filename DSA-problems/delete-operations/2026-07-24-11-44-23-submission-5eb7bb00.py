# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def process_operations(nums, operations):
  sorted_indices = []
  n = len(nums)
  for i in range(n):
    sorted_indices.append(i)
  deleted = set()
  sorted_indices.sort(key = lambda i:nums[i])
  smallest_idx = 0
  for op in operations:
    if 0 <= op < n:
      deleted.add(op)
    else:
      while smallest_idx < n and sorted_indices[smallest_idx] in deleted:
        smallest_idx += 1
      
      if smallest_idx < n:
        deleted.add(sorted_indices[smallest_idx])
        smallest_idx += 1
  res = []
  for i in range(n):
    if i not in deleted:
      res.append(nums[i])
  return res





