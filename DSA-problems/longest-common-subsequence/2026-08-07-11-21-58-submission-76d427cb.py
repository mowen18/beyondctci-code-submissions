# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def longest_common_subsequence(s1, s2):
  memo = {}
  def lcs(i1, i2):
    if i1 == len(s1) or i2 == len(s2):
      return 0
    
    if (i1, i2) in memo:
      return memo[(i1, i2)]
    
    if s1[i1] == s2[i2]:
      memo[(i1, i2)] = 1 + lcs(i1+1, i2+1)
    else:
      memo[(i1, i2)] = max(lcs(i1, i2+1), lcs(i1+1, i2))
    return memo[(i1, i2)]
  return lcs(0,0)

