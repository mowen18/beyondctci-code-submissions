# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def palindromic_sentence(s):
    l, r = 0, len(s) - 1
    while l < r:
      if not s[l].isalpha():
        l += 1
      elif not s[r].isalpha():
        r -= 1
      else:
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True
