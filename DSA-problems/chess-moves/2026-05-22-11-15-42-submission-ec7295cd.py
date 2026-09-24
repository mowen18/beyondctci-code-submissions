# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def is_valid(board, r, c):
    return 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] != 1

def chess_moves(board, piece, r, c):
    king_queen = [(1,0), (0,1), (-1,0), (0, -1), (-1, -1), (-1, 1), (1, -1), (1,1)]
    knight = [(2,1), (1,2), (-1, 2), (1, -2), (-2, 1), (2, -1), (-2, -1), (-1, -2)]
    res = []
    if piece == 'knight':
        for r_change, c_change in knight:
            if is_valid(board, r + r_change, c + c_change):
                new_r, new_c = r + r_change, c + c_change
                res.append([new_r, new_c])
    else:
        for r_change, c_change in king_queen:
            new_r, new_c = r_change + r, c_change + c
            if piece == 'king':
                if is_valid(board, new_r, new_c):
                    res.append([new_r, new_c])
            else:
                while is_valid(board, new_r, new_c):
                    res.append([new_r, new_c])
                    new_r += r_change
                    new_c += c_change
    return res






