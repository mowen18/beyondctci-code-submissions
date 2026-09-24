# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def longest_balanced_subsequence(s):
    stack = []
    invalid_ind = set()
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif not stack:
            invalid_ind.add(i)
        else:
            stack.pop()
    while stack:
        invalid_ind.add(stack.pop())
    res = []
    for i, c in enumerate(s):
        if i not in invalid_ind:
            res.append(c)
    
    return ''.join(res)


