# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def letter_occurrences(word):
  dic = {}
  for letter in word:
    if letter not in dic:
      dic[letter] = 0
    dic[letter] += 1
  
  tuples = []
  for letter, freq in dic.items():
    tuples.append((letter, freq))
  
  tuples.sort(key = lambda x: (-x[1], x[0]))
  res = []
  for letter, freq in tuples:
    res.append(letter)
  return res
  

    
