# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def is_valid_position(board):
  o_sum = 0
  x_sum = 0
  for row in board:
      for item in row:
          if item == "O":
              o_sum += 1
          elif item == "X":
              x_sum += 1
  if not (x_sum == o_sum or x_sum == o_sum + 1):
    return False
  def won(player):
    for row in board:
      if all(cell == player for cell in row):
        return True

    for c in range(len(board[0])):
      if all((board[r][c] == player for r in range(len(board)))):
        return True

    if all((board[i][i] == player for i in range(len(board)))):
      return True

    if all((board[i][len(board[0]) - 1 - i] == player for i in range(len(board)))):
      return True
    return False
  x_wins = won('X')
  o_wins = won('O')
  if o_wins and o_sum != x_sum:
    return False
  if x_wins and x_sum != o_sum + 1:
    return False
  if x_wins and o_wins:
    return False
  return True


