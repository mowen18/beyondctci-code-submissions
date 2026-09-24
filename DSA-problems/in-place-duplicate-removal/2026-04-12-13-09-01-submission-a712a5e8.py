# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def remove_duplicates(arr):
    s, w = 0, 0
    while s < len(arr):
      if s == 0 or arr[s] != arr[s-1]:
        arr[w] = arr[s]
        w += 1
      s += 1
    return w
