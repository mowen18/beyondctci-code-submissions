# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def count_subarrays_with_drops(arr, k):
   
    return [at_most(arr, k), exactly(arr, k), at_least(arr, k)]

  
def at_most(arr, k):
    l, r = 0, 0
    window = 0
    cnt = 0
    while r < len(arr):
        can_grow = r == 0 or arr[r] >= arr[r-1] or window < k
        if can_grow:
            if r > 0 and arr[r] < arr[r-1]:
                window += 1
            r += 1
            cnt += r - l
        else:
            if arr[l] > arr[l+1]:
                window -= 1
            l += 1
    return cnt
def at_least(arr, k):
    n = len(arr)
    n = n * (n + 1) // 2
    if k == 0:
        return n
    return n - at_most(arr, k-1)
def exactly(arr, k):
    if k == 0:
        return at_most(arr, k)
    return at_most(arr, k) - at_most(arr, k -1)




            

