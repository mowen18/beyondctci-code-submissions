# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def prefix_suffix_swap(arr):
    n = int(len(arr) / 3)
    r = n
    l = 0
    c = int(len(arr)/3) * 2

    while l < n:
      arr[l], arr[r] = arr[r], arr[l]
      l += 1
      r += 1
    while l < c:
      arr[l], arr[r] = arr[r], arr[l]
      l += 1
      r += 1
    return arr
    

