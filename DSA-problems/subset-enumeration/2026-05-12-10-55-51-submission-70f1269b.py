# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def all_subsets(S):
    res = []
    subsets = []
    def visit(idx):
      if idx == len(S):
        res.append(subsets[:])
        return
      subsets.append(S[idx])
      visit(idx + 1)
      subsets.pop()
      visit(idx + 1)
    visit(0)
    return res
