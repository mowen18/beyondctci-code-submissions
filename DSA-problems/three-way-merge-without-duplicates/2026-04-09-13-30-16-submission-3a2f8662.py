# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def three_way_merge(arr1, arr2, arr3):
    p1, p2, p3 = 0,0,0

    res = []
    
    while p1 < len(arr1) or p2 < len(arr2) or p3 < len(arr3):
        minval = float('inf')
        if p1 < len(arr1):
            minval = min(minval, arr1[p1])
        if p2 < len(arr2):
            minval = min(minval, arr2[p2])
        if p3 < len(arr3):
            minval = min(minval, arr3[p3])
        if p1 < len(arr1) and minval == arr1[p1]:
            p1 += 1
        if p2 < len(arr2) and minval == arr2[p2]:
            p2 += 1
        if p3 < len(arr3) and minval == arr3[p3]:
            p3 += 1
        if minval not in res:
            res.append(minval)
    return res

