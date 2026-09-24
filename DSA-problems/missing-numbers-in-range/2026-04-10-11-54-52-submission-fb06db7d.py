# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def missing_numbers(arr, low, high):
    res = []
    p1, p2 = 0, low
    while p1 < len(arr) and p2 <= high:
        if arr[p1] < p2:
            p1 += 1
        elif arr[p1] == p2:
            p1 += 1
            p2 += 1
        else:
            res.append(p2)
            p2 += 1
    if p2 <= high:
        res.extend(range(p2, high + 1))
    return res

        

        

    

    


