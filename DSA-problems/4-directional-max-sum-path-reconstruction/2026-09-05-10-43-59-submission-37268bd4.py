# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import math
def four_directional_max_sum_path_reconstruction(grid):
  best_sum = -math.inf
  r, c = len(grid), len(grid[0])
  seen = {(0,0)}
  best_path = []
  def visit(path, cursum):
    nonlocal best_sum, best_path
    currow, curcol = path[-1]
    if currow == r - 1 and curcol == c - 1:
      if cursum > best_sum:
        best_sum = cursum
        best_path = path.copy()
      return

    for nr, nc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
      new_row = currow + nr
      new_col = curcol + nc
      if (new_row, new_col) not in seen and 0 <= new_row < r and 0 <= new_col < c:
        seen.add((new_row, new_col))
        path.append((new_row, new_col))
        visit(path, cursum + grid[new_row][new_col])
        seen.remove((new_row, new_col))
        path.pop()
  start = (0,0)
  visit([start], grid[0][0])
  return best_path