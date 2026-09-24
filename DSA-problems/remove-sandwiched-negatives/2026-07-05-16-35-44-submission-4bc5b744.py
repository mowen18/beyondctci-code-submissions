# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def remove_sandwiched_negatives(arr):
  if len(arr) < 3:
    return len(arr)

  writer = 0
  seeker = 0

  while seeker < len(arr):
    # If we have a negative number between same positives
    if (seeker > 0 and seeker + 1 < len(arr) and
        arr[seeker] < 0 and
            arr[seeker - 1] == arr[seeker + 1]):
      seeker += 1  # Skip only the negative number
    else:
      arr[writer] = arr[seeker]
      writer += 1
      seeker += 1

  return writer
