# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def generate_permutations(arr):
    res = []
    perm = arr[:]
    def visit(i):
      if i == len(arr):
        res.append(perm[:])
        return
      for j in range(i, len(arr)):
        perm[i], perm[j] = perm[j], perm[i]
        visit(i + 1)
        perm[i], perm[j] = perm[j], perm[i]
    
    visit(0)
    return res

