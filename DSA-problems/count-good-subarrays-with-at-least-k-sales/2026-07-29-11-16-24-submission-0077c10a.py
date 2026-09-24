# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def count_good_subarrays_with_at_least_k_sales(sales, k):
  
  start = 0
  good_sub = []
  for i in range(len(sales)):
    if sales[i] < 10:
      if i > start:
        good_sub.append(sales[start:i])
      start = i + 1
  if start < len(sales):
    good_sub.append(sales[start:])
  
  def count_at_least(arr, k):
    n = len(arr)
    total = n * (n + 1) // 2
    if k == 0: return total
    return total - count_at_most(arr, k)
  def count_at_most(arr, k):
    l, r = 0, 0
    window_sum = 0
    count = 0
    while r < len(arr):
      window_sum += arr[r]
      r += 1
      while l < r and window_sum > k:
        window_sum -= arr[l]
        l += 1
      count += r - l
    return count
  cnt = 0
  for sub in good_sub:
    cnt += count_at_least(sub, k)
  return cnt




