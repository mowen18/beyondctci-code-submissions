# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
from collections import defaultdict
def max_at_most_k_distinct(best_seller, k):
  l, r = 0, 0
  book_freq = defaultdict(int)
  window_count = 0
  max_days = 0
  while r < len(best_seller):
    can_grow = best_seller[r] in book_freq or len(book_freq) + 1 <= k
    if can_grow:
      book_freq[best_seller[r]] += 1
      r += 1
      max_days = max(max_days, r-l)
    else:
      book_freq[best_seller[l]] -= 1
      if book_freq[best_seller[l]] == 0:
        del book_freq[best_seller[l]]
      r += 1
      l = r
  return max_days
      

