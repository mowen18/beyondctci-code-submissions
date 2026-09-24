# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def restaurant_ratings(ratings):
  n = len(ratings)
  memo = {}
  def rating_rec(i):
    if i >= n:
      return 0
    if i in memo:
      return memo[i]
    memo[i] = max(ratings[i] + rating_rec(i + 2), rating_rec(i + 1))
    return memo[i]
  return rating_rec(0)

