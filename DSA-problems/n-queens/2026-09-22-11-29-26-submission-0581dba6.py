# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def n_queens(n):
  queens = []
  count = 0

  def is_safe(new_row, new_col):

    for r, occupied_c in queens:
      if occupied_c == new_col:
        return False
      if abs(r - new_row) == abs(occupied_c - new_col):
        return False
    return True
  
  def visit(row):
    nonlocal count
    if row == n:
      count += 1
      return
    
    for col in range(n):
      if is_safe(row, col):
        queens.append((row, col))
        visit(row + 1)
        queens.pop()
  
  visit(0)
  return count

    

