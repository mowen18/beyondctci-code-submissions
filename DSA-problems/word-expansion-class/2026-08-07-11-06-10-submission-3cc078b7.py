# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
class Checker:
  def __init__(self, s):
    self.s = s

  def expands_into(self, s2):

    if len(self.s) != len(s2) - 1:
      return False
    freq = {}
    for c in s2:
      if c not in freq:
        freq[c] = 0
      freq[c] += 1
    
    for c in self.s:
      if c not in freq:
        return False
      freq[c] -= 1
      if freq[c] == 0:
        del freq[c]
    
    return len(freq) == 1 and list(freq.values())[0] == 1

    
