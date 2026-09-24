# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def nested_array_sum(arr):
    res = 0
    for elem in arr:
      if isinstance(elem, int):
        res += elem
      else:
        res += nested_array_sum(elem)
    return res

