# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def can_transform(word1, word2):
  if abs(len(word1) - len(word2)) != 1:
    return False
  if len(word1) > len(word2):
    word1, word2 = word2, word1

  for i in range(len(word2)):
    if word2[:i] + word2[i + 1:] == word1:
      return True
  return False

def build_graph(words, length1, length2):
  graph = {}
  for word in words:
    if len(word) in (length1, length2):
      graph[word] = []

  for word1 in graph:
    for word2 in graph:
      if word1 != word2 and can_transform(word1, word2):
        graph[word1].append(word2)
  
  return graph

def has_path(graph, start, end, visited = None):
  if visited is None:
    visited = set()
  if start == end and len(visited) == 0:
    return False
  if start == end and len(visited) > 0:
    return True
  visited.add(start)
  for nbr in graph[start]:
    if nbr not in visited and has_path(graph, nbr, end, visited):
      return True
  return False



def word_ladder_game(word1, word2, words):
    l = len(word1)
    l2 = len(word2)
    graph1 = build_graph(words, l, l + 1)
    if word2 in graph1 and has_path(graph1, word1, word2):
      return True
    
    graph2 = build_graph(words, l, l - 1)
    if word2 in graph2 and has_path(graph2, word1, word2):
      return True
    return False
