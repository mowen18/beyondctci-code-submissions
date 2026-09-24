# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def longest_alphabet_chain(arr):
  freqs = [0] * 26
  for i in range(len(arr)):
    freqs[ord(arr[i])-ord('a')] += 1
  
  minfreq = min(freqs)
  for i in range(len(freqs)):
    freqs[i] -= minfreq
  doubled = freqs + freqs
  l, r = 0, 0
  max_l = 0
  while r < len(doubled):
    can_grow = doubled[r] > 0
    if can_grow:
      r += 1
      max_l = max(max_l, r-l)
    else:
      r += 1
      l = r
  return 26 * minfreq + max_l
