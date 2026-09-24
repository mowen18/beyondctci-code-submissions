# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
from collections import defaultdict
def has_unique_k_days(best_seller, k):
    l, r = 0, 0
    bookfreq = defaultdict(int)
    while r < len(best_seller):
      bookfreq[best_seller[r]] += 1
      r += 1
      if r - l == k:
        if len(bookfreq) == k:
          return True
        bookfreq[best_seller[l]] -= 1
        if bookfreq[best_seller[l]] == 0:
          del bookfreq[best_seller[l]]
        l += 1
    return False
   
      
        
