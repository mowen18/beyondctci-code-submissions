# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def sort_colors(arr):
    rc = sum(1 for c in arr if c == 'R')
    wc = sum(1 for c in arr if c == 'W')
    for i in range(rc):
      arr[i] = 'R'
    for i in range(rc, rc + wc):
      arr[i] = 'W'
    for i in range(rc + wc, len(arr)):
      arr[i] = 'B'
    return arr
