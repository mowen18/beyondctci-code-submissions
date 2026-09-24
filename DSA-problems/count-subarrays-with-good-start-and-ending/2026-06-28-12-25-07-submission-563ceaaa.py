# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def count_subarrays_with_good_start_and_ending(sales):
  gd = 0
  ttl = 0
  for n in sales:
    if n >= 10:
      gd += 1
      ttl += gd
  return ttl

  

