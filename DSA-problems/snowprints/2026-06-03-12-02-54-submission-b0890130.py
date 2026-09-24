# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def snowprints(field):
    row, col = len(field), len(field[0])
    def is_valid(rn, cn):
        return 0 <= rn < row and 0 <= cn < col and field[rn][cn] == 1


    r, c = 0, 0
    while field[r][c] != 1:
        r += 1
    
    closest = r
    while c < col - 1:
        for r_dir in [1, 0, -1]:
            new_r = r + r_dir
            new_c = c + 1
            if is_valid(new_r, new_c):
                r, c = new_r, new_c
                closest = min(closest, new_r)
                break
    return closest
            



