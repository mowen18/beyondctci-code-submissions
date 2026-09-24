# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def alphabetic_sum_product(words, target):
  
  def alpha_sums(word):
    return sum(ord(c) - ord('a') + 1 for c in word)
  
  wordvals = set()

  for wrd in words:
    wordvals.add(alpha_sums(wrd))
  
  for val1 in wordvals:
    if target % val1 != 0:
      continue
    
    for val2 in wordvals:
      k = target / (val1 * val2)
      if k in wordvals:
        return True
  return False
