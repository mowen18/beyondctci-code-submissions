# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def google_colors(colors):
  if not colors: return []
  dic = {}
  for c in colors:
    if c in dic:
      dic[c].append(c)
    else:
      dic[c] = [c]
  
  res = []
  if "B" in dic:
    res.extend(dic["B"])
  if "R" in dic:
    res.extend(dic["R"])
  if "Y" in dic:
    res.extend(dic["Y"])
  if "G" in dic:
    res.extend(dic["G"])
  
  return res



