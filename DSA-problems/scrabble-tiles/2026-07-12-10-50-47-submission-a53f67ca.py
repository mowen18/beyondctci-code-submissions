# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def count_formable_words(dictionary, tiles):
  freqmap = {}
  for c in tiles:
    if c not in freqmap:
      freqmap[c] = 0
    freqmap[c] += 1
  res = 0
  for word in dictionary:
    dicfreq = {}
    for c in word:
      if c not in dicfreq:
        dicfreq[c] = 0
      dicfreq[c] += 1
    
    can_form = True
    for char, neededfreq in dicfreq.items():
      if char not in freqmap or neededfreq > freqmap[char]:
        can_form = False
        break
    if can_form == True:
      res += 1
  return res

    
    


