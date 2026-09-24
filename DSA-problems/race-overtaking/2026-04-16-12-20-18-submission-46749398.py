# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def race_overtaking(p1, p2):
    def is_before(i):
        return p1[i] > p2[i]
    l, r = 0, len(p2) - 1
    while r - l > 1:
        mid = (l + r) // 2
        if is_before(mid):
            l = mid
        else:
            r = mid
    return r

