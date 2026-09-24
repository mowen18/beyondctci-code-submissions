# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def count_0_sum_paths(grid):
  row, col = len(grid), len(grid[0])
  memo = {}
  def paths_rec(r, c):
    if r >= row or c >= col or grid[r][c] == 1:
      return 0
    if (r,c) in memo:
      return memo[(r,c)]
    if r == row - 1 and c == col - 1:
      return 1
    memo[(r,c)] = paths_rec(r + 1, c) + paths_rec(r, c+1) + paths_rec(r + 1, c+1)
    return memo[(r,c)]
  return paths_rec(0,0)

