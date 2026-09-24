# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def join(arr, s):
  char = ""
  for i in range(len(arr)):
    char += arr[i]
    if i < len(arr) - 1:
      char += s
  
  return char

