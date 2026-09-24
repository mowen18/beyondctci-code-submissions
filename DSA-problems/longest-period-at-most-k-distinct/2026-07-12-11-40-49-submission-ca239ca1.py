# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def max_at_most_k_distinct(best_seller, k):
  l, r = 0, 0
  max_days = 0
  window_cnt = {}
  while r < len(best_seller):
    can_grow = best_seller[r] in window_cnt or len(window_cnt) + 1 <= k
    if can_grow:
      if best_seller[r] not in window_cnt:
        window_cnt[best_seller[r]] = 0
      window_cnt[best_seller[r]] += 1
      r += 1
      max_days = max(max_days, r - l)
    else:
      window_cnt[best_seller[l]] -= 1
      if window_cnt[best_seller[l]] == 0:
        del window_cnt[best_seller[l]]
      
      l += 1
  return max_days

      

