# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def moves(seq):
    res = []
    idx = 0
    moves_rec(idx, res, seq)
    return "".join(res)
def moves_rec(idx, res, seq):
  if len(seq) == idx:
    return
  elif seq[idx] == '2':
    moves_rec(idx + 1, res, seq)
    moves_rec(idx + 2, res, seq)
  else:
    res.append(seq[idx])
    moves_rec(idx + 1, res, seq)

