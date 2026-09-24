# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def count_substrings_without_letter(s):
  def op(k):
    return k*(k+1)/2
  sections = s.split('a')
  res = []
  for sec in sections:
    res.append(op(len(sec)))
  
  return sum(res)


