# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def all_overbooked_slots(slots, bookings, cap):
  for l, r, c in bookings:
    for i in range(l, r + 1):
      slots[i] += c
  cnt = 0
  for bk in slots:
    if bk > cap:
      cnt += 1
  return cnt
