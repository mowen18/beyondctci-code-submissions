# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import random
def quicksort(arr):
  if len(arr) <= 1:
    return arr
  
  small, equal, large = partition(arr)

  return quicksort(small) + equal + quicksort(large)

def partition(arr):
  pivot = arr[random.randint(0, len(arr) - 1)]
  small = []
  equal = []
  large = []
  for num in arr:
    if num > pivot:
      large.append(num)
    elif num == pivot:
      equal.append(num)
    else:
      small.append(num)
  return small, equal, large



