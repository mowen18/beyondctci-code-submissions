# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def first_false(arr):
    if len(arr) < 1:
        return -1
    l, r = 0, len(arr) - 1

    while l < r:
        mid = (l + r) // 2
        if arr[mid] == False:
            r = mid
        else:
            l = mid + 1
    
    if arr[l] == True:
        return -1
    return l
