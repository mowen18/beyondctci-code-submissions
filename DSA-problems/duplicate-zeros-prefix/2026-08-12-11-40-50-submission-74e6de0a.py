# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def duplicate_zeros_prefix(arr):
  def prefix(arr):
    fast, slow = 0, 0
    while fast < len(arr):
      if arr[slow] == 0:
        if fast + 2 > len(arr):
          return slow, True

        fast += 2
      
      else:
        fast += 1
      
      slow += 1
    return slow - 1, False
  
  seeker, half_expanded = prefix(arr)
  writer = len(arr) - 1
  if half_expanded:
    arr[writer] = 0
    writer -= 1
    seeker -= 1
  
  while seeker >= 0:
    if arr[seeker] == 0:
      arr[writer] = 0
      arr[writer - 1] = 0
      writer -= 2
    else:
      arr[writer] = arr[seeker]
      writer -= 1
    seeker -= 1
  


