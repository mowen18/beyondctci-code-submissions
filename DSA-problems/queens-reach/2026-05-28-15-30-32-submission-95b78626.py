# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def safe_cells(board):
  dirs = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (-1,-1), (-1, 1), (1,-1)]
  def is_valid(rw, cl):
    return 0 <= rw < len(board) and 0 <= cl < len(board[0]) and board[rw][cl]==0

  queens = []
  r, c = len(board), len(board[0])
  for row in range(r):
    for col in range(c):
      if board[row][col] == 1:
        queens.append((row, col))
  newb = [[0] * c  for _ in range(r)]
  for row, col in queens:
    newb[row][col] = 1
    for r_move, c_move in dirs:
      newr = row + r_move
      newc = col + c_move
      while is_valid(newr, newc):
        newb[newr][newc] = 1
        newr += r_move
        newc += c_move
  return newb
      


