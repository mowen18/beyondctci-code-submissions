# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def longest_repeated_substring(s):
  def repeated(k):
    rep = set()
    for i in range(len(s) - k + 1):
      st = s[i: i + k]
      if st in rep:
        return st
      rep.add(st)
    return None
  
  l, r = 0, len(s)
  best = ""
  while r - l > 1:
    mid = (r + l) // 2
    scan = repeated(mid)
    if scan is not None:
      best = scan
      l = mid
    else:
      r = mid
  return best


