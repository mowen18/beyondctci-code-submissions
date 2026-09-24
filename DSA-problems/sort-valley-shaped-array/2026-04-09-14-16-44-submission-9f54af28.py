# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def sort_valley_array(arr):
    res = [0] * len(arr)
    l, r = 0, len(arr) - 1
    i = len(res) - 1
    if not arr:
        return []
    while l < r:
        if arr[l] >= arr[r]:
            res[i] = arr[l]
            l += 1
            i -= 1
        else:
            res[i] = arr[r]
            r -= 1
            i -= 1
    res[0] = arr[l]
    return res


