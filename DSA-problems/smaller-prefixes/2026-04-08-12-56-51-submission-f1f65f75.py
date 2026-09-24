# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def smaller_prefixes(arr):
    sp, fp = 0, 0
    small_sum, large_sum = 0, 0
    while fp < len(arr):
        small_sum += arr[sp]
        large_sum += arr[fp] + arr[fp+1]
        if small_sum > large_sum:
            return False
        sp += 1
        fp += 2
    return True
