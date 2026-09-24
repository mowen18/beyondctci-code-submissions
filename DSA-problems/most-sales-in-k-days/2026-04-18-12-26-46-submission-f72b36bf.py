# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def most_sales_in_k_days(sales, k):
    l, r = 0, 0
    currwindow = 0
    maxwindow = 0
    maxidx = 0
    while r < len(sales):
      currwindow += sales[r]
      r += 1
      if r - l == k:
        if maxwindow < currwindow:
          maxidx = l
        maxwindow = max(maxwindow, currwindow)
        currwindow -= sales[l]
        l += 1
    return maxidx
        


