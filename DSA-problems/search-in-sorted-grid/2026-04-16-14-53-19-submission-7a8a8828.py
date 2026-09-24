# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def search_in_sorted_grid(grid, target):
    num_col = len(grid[0])
    l, r = 0, len(grid[0]) * len(grid) - 1
    if grid[0][0] == target:
      return [0,0]
    if grid[len(grid)-1][len(grid[0])-1] == target:
      return [len(grid)-1, len(grid[0])-1]
    def is_before(mid):
      row, col = mid // num_col, mid % num_col
      return grid[row][col] < target
    while r - l > 1:
      mid = (l + r) // 2
      if is_before(mid):
        l = mid
      else:
        r = mid
    row, col = r // num_col, r % num_col
    if grid[row][col] == target:
      return [row,col]
    return [-1, -1]
    

