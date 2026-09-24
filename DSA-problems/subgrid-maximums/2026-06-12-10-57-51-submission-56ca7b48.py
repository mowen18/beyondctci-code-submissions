# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import math
def subgrid_maximums(grid):
  R, C = len(grid), len(grid[0])
  res = [row.copy() for row in grid]
  for r in range(R - 1, -1, -1):
    for c in range(C-1, -1, -1):
      if r + 1 < R:
        res[r][c] = max(res[r][c], res[r+1][c])
      if c + 1 < C:
        res[r][c] = max(res[r][c], res[r][c+1])
  return res

