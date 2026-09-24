# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def most_booked_slot(slots, bookings):
  n = len(slots)
  diff = [0] * n
  for l, r, c in bookings:
    diff[l] += c
    if r + 1 < n:
      diff[r + 1] -= c
  prefix_sums = [0] * n
  prefix_sums[0] = diff[0]
  for i in range(1, n):
    prefix_sums[i] = prefix_sums[i-1] + diff[i]
  maxslot = 0
  for i in range(n):
    prefix_sums[i] += slots[i]
    if prefix_sums[i] > prefix_sums[maxslot]:
      maxslot = i
  return maxslot

