# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def channel_views(views, periods):
    prefix_sums = []
    if not views:
      return []
    prefix_sums.append(views[0])
    for i in range(1, len(views)):
      prefix_sums.append(prefix_sums[i - 1] + views[i])
    res = []
    for i, j in periods:
      if i == 0:
        res.append(prefix_sums[j])
      else:
        res.append(prefix_sums[j] - prefix_sums[i - 1])
    return res
    

   

