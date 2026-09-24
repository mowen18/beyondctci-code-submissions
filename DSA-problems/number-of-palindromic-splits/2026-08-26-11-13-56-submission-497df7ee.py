# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def number_of_palindromic_splits(s):
  if len(s) == 0:
    return 0
  def dp(i):
    if i == len(s):
      return 1
    count = 0
    for j in range(i, len(s)):
      subst = s[i:j+1]
      if subst == subst[::-1]:
        count += dp(j + 1)
    return count
  return dp(0)

    

