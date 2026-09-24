# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def min_subarray_sum_split(arr, k):
    def get_num_splits(arr, max_s):
      current_sum = 0
      splits = 1
      for num in arr:
        if current_sum + num > max_s:
          splits += 1
          current_sum = num
        else:
          current_sum += num
      return splits
    
    def is_before(arr, k, max_s):
      return get_num_splits(arr, max_s) > k
    
    l, r = max(arr), sum(arr)
    if is_before(arr, k, l) == False:
        return l
        
    while r - l > 1:
      mid = (l + r) // 2
      if is_before(arr, k, mid):
        l = mid
      else:
        r = mid
    return r
      
      
      
    


