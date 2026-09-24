# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def add_total_digits(n):
  if n < 10: return n

  return n % 10 + add_total_digits(n // 10)
