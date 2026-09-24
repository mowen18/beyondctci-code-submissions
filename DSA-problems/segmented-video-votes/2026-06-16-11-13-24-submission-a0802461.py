# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def segmented_video_votes(n, votes):
    diff = [0 for _ in range(n)]

    for l, r, v in votes:
        diff[l] += v
        if r + 1 < n:
            diff[r + 1] -= v
    
    prefixsums = [0 for _ in range(n)]
    prefixsums[0] = diff[0]
    for i in range(1, n):
        prefixsums[i] = prefixsums[i-1] + diff[i]
    
    return prefixsums
