# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
from collections import Counter
def count_unique_submultisets_with_sum_zero(S):
  
  frequency = Counter(S)
  
  unique_elements = list(frequency.keys())
  
  def rec(index, current_sum):
    if index == len(unique_elements):
      return 1 if current_sum == 0 else 0 
   
    element = unique_elements[index]
    count = frequency[element]
    total_sum = 0
    
    for i in range(count + 1):
      total_sum += rec(index + 1, current_sum + i * element)
    return total_sum

  return rec(0,0)


