# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def max_at_most_k_distinct(best_seller, k):
    l, r = 0, 0
    book_freq = {}
    max_days = 0
    while r < len(best_seller):
      can_grow = best_seller[r] in book_freq or len(book_freq) + 1 <= k
      if can_grow:
        if best_seller[r] not in book_freq:
          book_freq[best_seller[r]] = 0
        book_freq[best_seller[r]] += 1
        r += 1
        max_days = max(max_days, r - l)
      
      else:
        book_freq[best_seller[l]] -= 1
        if book_freq[best_seller[l]] == 0:
          del book_freq[best_seller[l]]
        l += 1
    return max_days

