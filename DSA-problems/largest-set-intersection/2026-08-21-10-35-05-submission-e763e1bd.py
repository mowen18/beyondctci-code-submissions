# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import math
def largest_set_intersection(sets):
    freq = {}
    for i in sets:
        for j in i:
            if j not in freq:
                freq[j] = 0
            freq[j] += 1
    
    n = len(sets)
    mincount = math.inf
    best_index = 0
    for i, s in enumerate(sets):
        count = sum(1 for x in s if freq[x] == n - 1)
        if count < mincount:
            mincount = count
            best_index = i
    return best_index



