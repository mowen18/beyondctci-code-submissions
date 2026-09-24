# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.

def max_sum_path_backtracking(grid):
  row, col = len(grid), len(grid[0])
  memo = {}
  def max_path_rec(r, c):
    if r == row - 1 and c == col - 1:
      return grid[r][c]
    if (r,c) in memo:
      return memo[(r,c)]
    elif c == col - 1:
      memo[(r,c)] = grid[r][c] + max_path_rec(r + 1, c)
    elif r == row - 1:
      memo[(r,c)]  = grid[r][c] + max_path_rec(r, c + 1)
    else:
      memo[(r,c)]  = grid[r][c] + max(max_path_rec(r + 1, c), max_path_rec(r, c + 1))
    return memo[(r,c)]
  return max_path_rec(0,0)


    
  
    
