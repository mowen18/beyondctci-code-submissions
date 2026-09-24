# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def move_subsequence(arr, word):
  seeker, writer = 0, 0
  i = 0
  while seeker < len(arr):
    if i < len(word) and word[i] == arr[seeker]:
      seeker += 1
      i += 1
    else:
      arr[writer] = arr[seeker]
      writer += 1
      seeker += 1
  k = len(word)
  for i in range(writer - 1, -1, -1):
    arr[i + k] = arr[i]
  
  for i in range(k):
    arr[i] = word[i]
  
