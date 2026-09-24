# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def number_of_palindromic_splits(s):
  if len(s) == 0:
    return 0
  def find_palindromes(s):
    n = len(s)
    palindromes = []
    for i in range(n):
      l, r = i, i
      while l >= 0 and r < n and s[l] == s[r]:
        palindromes.append((l, r))
        l -= 1
        r += 1
      l, r = i, i + 1
      while l >= 0 and r < n and s[l] == s[r]:
        palindromes.append((l, r))
        l -= 1
        r += 1
    return palindromes
  """
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
  """
  def top_sort(graph):
    V = len(graph)
    in_degree = [0 for _ in range(V)]
    for node in range(V):
      for nbr in graph[node]:
        in_degree[nbr] += 1
    deg_zero = []
    for node in range(V):
      if in_degree[node] == 0:
        deg_zero.append(node)
    
    tops = []
    while deg_zero:
      node = deg_zero.pop()
      tops.append(node)
      for nbr in graph[node]:
        in_degree[nbr] -= 1
        if in_degree[nbr] == 0:
          deg_zero.append(nbr)
    return tops
  pals = find_palindromes(s)
  n = len(s)
  graph = [[] for _ in range(n + 1)]
  for l, r in pals:
    graph[l].append(r+1)
  
  toporder = top_sort(graph)
  counts = [0] * (n+1)
  counts[0] = 1
  for node in toporder:
    for nbr in graph[node]:
      counts[nbr] += counts[node]
  return counts[n]
  



    

