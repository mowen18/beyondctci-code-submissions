# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def target_count_divisible_by_k(arr, target, k):
    def first():
        l, r = 0, len(arr) - 1
        if len(arr) > 0 and target == arr[l]:
            return l
        if not arr:
            return -1
        while r - l > 1:
            mid = (l + r) // 2
            if arr[mid] < target:
                l = mid
            else:
                r = mid
        if arr[r] == target:
            return r
        return -1
    def last():
        l, r = 0, len(arr) - 1
        if arr[r] == target:
            return r
        while r - l > 1:
            mid = (r + l) // 2
            if arr[mid] == target:
                l = mid
            else:
                r = mid
        return l
        
    l, r = first(), last()
    if l == -1 or r == -1:
        return True
    return (((r - l) + 1) % k) == 0


