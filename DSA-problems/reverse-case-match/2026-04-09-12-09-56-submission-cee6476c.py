# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def reverse_case_match(s):
    l, r = 0, len(s) - 1
    while l < len(s) and r > -1:
      if s[l].isupper():
        l += 1
      elif s[r].islower():
        r -= 1
      elif s[l] == s[r].lower():
        l += 1
        r -= 1
      else:
          return False
    return True
      
      
