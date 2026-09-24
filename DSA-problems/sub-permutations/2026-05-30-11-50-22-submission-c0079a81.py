# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def sub_permutations(s1, s2):
  if len(s1) > len(s2):
    return 0
  dic = {}
  for c in s1:
    if c not in dic:
      dic[c] = 0
    dic[c] += 1
  perms = set()
  l, r = 0, 0
  while r < len(s2):
    c = s2[r]
    if c not in dic:
      dic[c] = 0
    dic[c] -= 1
    if dic[c] == 0:
      del dic[c]
    r += 1

    if r - l == len(s1):
      if not dic:
        perms.add(s2[l:r])

      c = s2[l]
      if c not in dic:
        dic[c] = 0
      dic[c] += 1
      if dic[c] == 0:
        del dic[c]
      l += 1
  return len(perms)
  

 