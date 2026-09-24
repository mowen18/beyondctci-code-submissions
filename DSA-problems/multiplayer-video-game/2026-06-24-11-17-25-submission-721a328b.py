# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def multiplayer_video_game(players):
  x_groups = {}
  graph = [[] for _ in range(len(players))]
  for i, (x,y) in enumerate(players):
    if x not in x_groups:
      x_groups[x] = []
    x_groups[x].append((y, i))
  y_groups = {}
  for i, (x,y) in enumerate(players):
    if y not in y_groups:
      y_groups[y] = []
    y_groups[y].append((x,i))
  
  for x in x_groups:
    points = sorted(x_groups[x])
    for i in range(len(points)-1):
      graph[points[i][1]].append(points[i+1][1])
      graph[points[i+1][1]].append(points[i][1])
  for y in y_groups:
    points = sorted(y_groups[y])
    for i in range(len(points)-1):
      graph[points[i][1]].append(points[i+1][1])
      graph[points[i+1][1]].append(points[i][1])
  visited = set()

  def visit(node):
    for nbr in graph[node]:
      if nbr not in visited:
        visited.add(nbr)
        visit(nbr)
  count = 0
  for node in range(len(graph)):
    if node not in visited:
      visited.add(node)
      visit(node)
      count += 1
  return count