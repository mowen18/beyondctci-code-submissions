# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def longest_consecutive_sequence(arr):
  nums = set(arr)
  maxseq = 0
  for num in arr:
    if num - 1 not in nums:
      current = num
      length = 1
      while current + 1 in nums:
        current += 1
        length += 1
      maxseq = max(maxseq, length)
  return maxseq
      

