# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def all_overbooked_slots(slots, bookings, cap):
  diff = [0] * len(slots)
  for l, r, c in bookings:
    diff[l] += c
    if r + 1 < len(slots):
      diff[r+1] -= c
  
  prefix_sums = [0] * len(slots)
  prefix_sums[0] = diff[0]
  for i in range(1, len(slots)):
    prefix_sums[i] = prefix_sums[i-1] + diff[i]
  
  numover = 0
  for i in range(len(slots)):
    if slots[i] + prefix_sums[i] > cap:
      numover += 1
  
  return numover


