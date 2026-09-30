# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def matrix_rotation(mat):
  n = len(mat)
  for r in range(n):
    for c in range(r):
      mat[r][c], mat[c][r] = mat[c][r], mat[r][c]
  
  for r in range(n):
    for c in range(n//2):
      mat[r][c], mat[r][n-c-1] = mat[r][n-c-1], mat[r][c]

