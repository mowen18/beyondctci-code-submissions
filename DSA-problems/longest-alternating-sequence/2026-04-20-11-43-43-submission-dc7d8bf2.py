# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def longest_alternating_sequence(sales):
    l, r = 0, 0
    cnt = 1
    max_cnt = 0
    if not sales:
      return 0
  
    while r < len(sales):
      can_move_cnt = l == r or (sales[r] > 9 and sales[r-1] < 10) or (sales[r] < 10 and sales[r-1] > 9)
      if can_move_cnt:
        r +=1
        max_cnt = max(max_cnt, r - l)
      else:
        l += 1
        r += 1
    return max_cnt

