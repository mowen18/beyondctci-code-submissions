# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def count_subarrays_with_at_least_k_bad_days(sales, k):
  n = len(sales)
  if n == 0:
    return 0
  total_sub_arrays = n * (n + 1) // 2
  if k == 0:
    return total_sub_arrays
  return total_sub_arrays - count_at_most_k_bad_days(sales, k - 1)

def count_at_most_k_bad_days(sales, k):
  l, r = 0, 0
  cnt = 0
  curwindow = 0
  while r < len(sales):
    can_grow = sales[r] >= 10 or curwindow < k
    if can_grow:
      if sales[r] < 10:
        curwindow += 1
      r += 1
      cnt += r - l
    else:
      if sales[l] < 10:
        curwindow -= 1
      l += 1
  return cnt