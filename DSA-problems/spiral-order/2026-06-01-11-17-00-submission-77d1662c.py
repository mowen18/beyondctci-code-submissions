# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def spiral_order(n):
  
  def is_valid(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 0
  
  res = [[0]* n for _ in range(n)]
  val = n * n - 1
  directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
  r, c = n - 1, n - 1
  dirs = 0
  while val > 0:
    res[r][c] = val
    if not is_valid(res, r + directions[dirs][0], c + directions[dirs][1]):
      dirs = (dirs + 1) % 4
    r, c = r + directions[dirs][0], c + directions[dirs][1]
    val -= 1
  return res



