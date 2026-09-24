# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def subgrid_sums(grid):
  R, C = len(grid), len(grid[0])
  newgrid = [[0] * C for _ in range(R)]
  for r in range(R - 1, -1, -1):
    for c in range(C - 1, -1, -1):
      cursum = grid[r][c]
      if r + 1 < R:
        cursum += newgrid[r+1][c]
      if c + 1 < C:
        cursum += newgrid[r][c+1]
      if r + 1 < R and c + 1 < C:
        cursum -= newgrid[r + 1][c + 1]
      newgrid[r][c] = cursum
  return newgrid

      


