# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def tilings(n):
  memo = {}
  def dp(i):
    if i <= 1:
      return 1
    if i in memo:
      return memo[i]
    memo[i] = dp(i - 1) + dp(i - 2)
    return memo[i]
  
  return dp(n)
