# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.

def max_laminal_sum(arr):

  def max_sum(l,r):
    if r - l == 1:
      return arr[l]
    mid = (l + r) // 2
    option1 = max_sum(l, mid)
    option2 = max_sum(mid, r)
    option3 = sum(arr[l:r])
    return max(option1, option2, option3)
  
  return max_sum(0, len(arr))


