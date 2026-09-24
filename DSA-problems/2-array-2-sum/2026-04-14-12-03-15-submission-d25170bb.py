# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def two_array_two_sum(sorted_arr, unsorted_arr):
    for i in range(len(unsorted_arr)):
      l, r = 0, len(sorted_arr) - 1
      while r - l > 1:
        mid = (r + l) // 2
        if sorted_arr[r] + unsorted_arr[i] > 0:
          r = mid
        else:
          l = mid
      if sorted_arr[r] + unsorted_arr[i] == 0:
        return [r, i]
      elif sorted_arr[l] + unsorted_arr[i] == 0:
        return [l, i]
      else:
        continue

    return [-1,-1]
