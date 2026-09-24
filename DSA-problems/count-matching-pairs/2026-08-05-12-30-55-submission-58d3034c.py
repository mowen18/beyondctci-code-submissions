# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def count_matching_pairs(s):
  if len(s) < 3: return 0
  count = 0
  if s[0] == s[2]:
    count = 1
  return count + count_matching_pairs(s[1:])

