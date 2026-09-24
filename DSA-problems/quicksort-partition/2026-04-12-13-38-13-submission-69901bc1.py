# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def partition(arr, pivot):
    l, r = 0, len(arr) - 1
    while l < r:
      if arr[l] <= pivot:
        l += 1
      elif arr[r] > pivot:
        r -= 1
      else:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    l, r = 0, len(arr) - 1
    while l < r:
      if arr[l] < pivot:
        l += 1
      elif arr[r] >= pivot:
        r -= 1
      else:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    return arr

