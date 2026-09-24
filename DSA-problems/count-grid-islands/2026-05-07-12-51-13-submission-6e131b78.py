# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def grid_dfs(grid, visited, r, c):
  
  def is_valid(r, c):
    if r < 0 or c < 0:
      return False
    if r < len(grid) and c < len(grid[0]) and (r, c) not in visited and grid[r][c] == 1:
      return True
    return False
  directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
  def visit(r, c):
    for dr, dc in directions:
      nr, nc = r + dr, c + dc
      if is_valid(nr, nc) and (nr, nc) not in visited:
        visited.add((nr, nc))
        visit(nr, nc)
  visit(r, c)

def count_islands_in_place(grid):
    visited = set()
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    for row in range(rows):
      for col in range(cols):
        if grid[row][col] == 1 and (row,col) not in visited:
          visited.add((row,col))
          grid_dfs(grid, visited, row, col)
          count += 1
    return count

