# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def count_adjacent_numbers(n):
  
  if n == 0:
    return 0
  
  last = n % 10
  rest = n // 10
  if last == 1:
    return 1 + count_adjacent_numbers(rest)
  return count_adjacent_numbers(rest)
