# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def validate_matrix_rows_columns(matrix):
  if not matrix: return False
  n = len(matrix)
  for row in matrix:
    seen = set()
    for val in row:
      if val < 1 or val > n or val in seen:
        return False
      seen.add(val)
  
  for r in range(n):
    seen = set()
    for c in range(n):
      val = matrix[c][r]
      if val > n or val < 1 or val in seen:
        return False
      seen.add(val)
  return True


