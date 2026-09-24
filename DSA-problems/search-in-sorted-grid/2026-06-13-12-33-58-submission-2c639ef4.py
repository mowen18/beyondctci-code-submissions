# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def search_in_sorted_grid(grid, target):
  R, C = len(grid), len(grid[0])

  def is_before(i):
    row = i // C
    col = i % C
    return grid[row][col] < target
  
  if grid[0][0] > target:
    return [-1,-1]
  if grid[R- 1][C-1] < target:
    return [-1,-1]
  if grid[0][0] == target:
    return [0,0]
  l , r = 0, R * C - 1
  while r - l > 1:
    mid = (l + r) // 2
    if is_before(mid):
      l = mid
    else:
      r = mid
  rw = r // C
  cl = r % C
  if grid[rw][cl] != target:
    return [-1, -1]
  return [rw,cl]


