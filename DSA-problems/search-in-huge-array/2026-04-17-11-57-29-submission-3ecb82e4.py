# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def find_through_api(target, fetch):
    def is_before(idx):
        return fetch(idx) != -1 and fetch(idx) < target
    l, r = 0, 1
    if fetch(l) == target:
        return l
    if fetch(l) == -1:
        return -1
    while is_before(r):
        r *= 2
    while r - l > 1:
        mid = (l+r) // 2
        if is_before(mid):
            l = mid
        else:
            r = mid
    if fetch(r) == target:
        return r
    return -1

