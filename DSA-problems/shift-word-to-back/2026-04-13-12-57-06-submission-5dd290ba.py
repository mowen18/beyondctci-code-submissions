# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def move_word(arr, word):
    i = 0
    seeker, writer = 0, 0
    while seeker < len(arr):
      if i < len(word) and arr[seeker] == word[i]:
        seeker += 1
        i += 1
      else:
        arr[writer] = arr[seeker]
        writer += 1
        seeker += 1
    for w in word:
      arr[writer] = w
      writer += 1
