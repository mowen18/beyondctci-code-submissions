# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def company_launches(launches, ads):
  data = [(launches[i], ads[i], i) for i in range(len(launches))]
  data.sort()
  highest = -1
  second = -1
  res = []
  for l, spend, idx in data:
    if spend > highest:
      second = highest
      highest = spend
    elif spend > second:
      second = spend
      res.append(idx)
  return res
