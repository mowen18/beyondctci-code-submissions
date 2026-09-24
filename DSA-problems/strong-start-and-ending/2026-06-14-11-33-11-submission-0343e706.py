# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def max_good_days_start_and_end_sliding_window(projected_sales, k):
  n = len(projected_sales)
  B = sum(1 for x in projected_sales if x < 10)
  if B <= k:
    return len(projected_sales)
  suffix_ptr = n
  suffix_bad = 0
  for i in range(n-1, -1, -1):
    if projected_sales[i] < 10:
      if suffix_bad < k:
        suffix_bad += 1
      else:
        suffix_ptr = i + 1
        break
  prefix_ptr = 0
  prefix_bad = 0
  res = n - suffix_ptr
  for prefix_ptr in range(n):
    if projected_sales[prefix_ptr] < 10:
      prefix_bad += 1
      while prefix_bad + suffix_bad > k and suffix_ptr < n:
        if projected_sales[suffix_ptr] < 10:
          suffix_bad -= 1
        suffix_ptr += 1

        if prefix_bad > k:
          break
        prefix_length = prefix_ptr + 1
        suffix_length = n - suffix_ptr

        res = max(res, prefix_length + suffix_length)
  return res



      
  

