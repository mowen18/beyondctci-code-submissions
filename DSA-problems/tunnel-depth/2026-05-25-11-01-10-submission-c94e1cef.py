# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.


def tunnel_depth(tunnel_network):
  def is_before(row):
    return 1 in tunnel_network[row]
  
  l, r = 0, len(tunnel_network) - 1
  if is_before(r):
    return r
  

  while r - l > 1:
    mid = (l + r) // 2
    if is_before(mid):
      l = mid
    else:
      r = mid
  return l

