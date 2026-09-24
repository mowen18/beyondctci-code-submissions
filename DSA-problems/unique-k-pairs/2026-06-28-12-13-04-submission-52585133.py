# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def unique_k_pairs(numbers, difference):
  dic = {}
  for num in numbers:
    dic[num] = dic.get(num, 0) + 1
  
  s = set()
  for n in numbers:
    if difference > 0:
      if n + difference in dic:
        s.add(tuple([n, n + difference]))
    else:
      if dic[n] > 1:
        s.add(tuple([n, n]))
  return s
  


  
