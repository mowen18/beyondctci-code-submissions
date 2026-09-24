# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def all_subsets(S):
    res = []
    subset = []
    def visit(idx):
      if idx == len(S):
        res.append(subset.copy())
        return
      subset.append(S[idx])
      visit(idx + 1)
      subset.pop()
      visit(idx + 1)
    visit(0)
    return res
