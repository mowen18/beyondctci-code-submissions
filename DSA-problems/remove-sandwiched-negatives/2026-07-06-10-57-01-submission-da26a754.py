# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def remove_sandwiched_negatives(arr):
    seeker, writer = 0,0
    while seeker < len(arr):
      if (seeker > 0 and seeker < len(arr) - 1) and (arr[seeker] < 0 and arr[seeker - 1] == arr[seeker + 1]):
        seeker += 1
      else:
        arr[writer] = arr[seeker]
        writer += 1
        seeker += 1
    return writer
