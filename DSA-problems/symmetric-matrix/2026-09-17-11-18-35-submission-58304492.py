# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def is_symmetric(matrix):
  if len(matrix) == 0: return False
  if len(matrix) != len(matrix[0]): return False

  for r in range(len(matrix)):
    for c in range(len(matrix)):

      if matrix[r][c] != matrix[c][r]: return False
  
  return True



