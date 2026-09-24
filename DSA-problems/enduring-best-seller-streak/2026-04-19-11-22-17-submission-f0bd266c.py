# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
from collections import defaultdict
def has_enduring_best_seller_streak_2(best_seller, k):
    l, r = 0, 0
    sellers = defaultdict(int)
    while r < len(best_seller):
      sellers[best_seller[r]] += 1
      r += 1
      if r - l == k:
        if len(sellers) == 1:
          return True
        sellers[best_seller[l]] -= 1
        if sellers[best_seller[l]] == 0:
          del sellers[best_seller[l]]
        l += 1
    return False
