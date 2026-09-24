# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def valid_sudoku(board):
  return valid_rows(board) and valid_cols(board) and valid_subgrid(board)

def valid_rows(board):
  R, C = len(board), len(board[0])

  for r in range(R):
    seen = set()
    for c in range(C):
      if board[r][c] in seen:
        return False
      if board[r][c] != 0:
        seen.add(board[r][c])
  return True
def valid_cols(board):
  R, C = len(board), len(board[0])

  for c in range(C):
    seen = set()
    for r in range(R):
      if board[r][c] in seen:
        return False
      if board[r][c] != 0:
        seen.add(board[r][c])
  return True
def valid_subgrid(board):
  for r in range(3):
    for c in range(3):
      if not validgrid(board, r * 3, c * 3):
        return False
  return True



def validgrid(board, rw, cl):
  seen = set()
  for r in range(rw, rw + 3):
    for c in range(cl, cl + 3):
      if board[r][c] in seen:
        return False
      if board[r][c] != 0:
        seen.add(board[r][c])
  return True



