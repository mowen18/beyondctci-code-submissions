# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def most_booked_slot(slots, bookings):
  numbookings = [0 for _ in range(len(slots))]

  for l, r, c in bookings:
    numbookings[l] += c
    if r + 1 < len(slots):
      numbookings[r+1] -= c
    
  prefixsums = [0 for _ in range(len(slots))]
  prefixsums[0] = numbookings[0]
  for i in range(1, len(numbookings)-1):
    prefixsums[i] = prefixsums[i-1] + numbookings[i]
  maxindex = 0
  for i in range(len(slots)):
    prefixsums[i] += slots[i]
    if prefixsums[i] > prefixsums[maxindex]:
      maxindex = i
  return maxindex
  
