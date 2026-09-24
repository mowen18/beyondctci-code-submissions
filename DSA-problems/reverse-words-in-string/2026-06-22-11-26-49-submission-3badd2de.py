# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def reverse_words(sentence):
  chars = list(sentence)
  n = len(chars)

  seeker, writer = 0, 0
  while seeker < n:

    while seeker < n and chars[seeker] == " ":
      seeker += 1
    
    if seeker == n:
      break
    
    if writer > 0:
      chars[writer] = ' '
      writer += 1
    
    while seeker < n and chars[seeker] != " ":
      chars[writer] = chars[seeker]
      writer += 1
      seeker += 1
  
  chars = chars[:writer]

  l, r = 0, len(chars) - 1
  while l < r:
    chars[l], chars[r] = chars[r], chars[l]
    l += 1
    r -= 1
  
  l = 0
  #r = 0
  while l < len(chars):
    r = l
    while r < len(chars) and chars[r] != ' ':
      r += 1
    w_l = l
    w_r = r - 1
    while w_l < w_r:
      chars[w_l], chars[w_r] = chars[w_r], chars[w_l]
      w_l += 1
      w_r -= 1
    l = r + 1
  
  return ''.join(chars)
    


