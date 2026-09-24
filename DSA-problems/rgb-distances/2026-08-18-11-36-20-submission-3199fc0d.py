# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
from collections import deque

def get_sources(screen, target):
  sources = []
  for i in range(len(screen)):
    for j in range(len(screen[0])):
      if screen[i][j] == target:
        sources.append((i,j))
  return sources

def bfs(screen, sources):
  rows, cols = len(screen), len(screen[0])
  q = deque()
  distances = {}
  for i, j in sources:
    q.append((i,j))
    distances[(i, j)] = 0
  
  while q:
    r, c = q.popleft()
    for nr, nc in [(r + 1, c), (r-1, c), (r, c + 1), (r, c - 1)]:
      if 0 <= nr <= rows and 0 <= nc <= cols and (nr, nc) not in distances:
        distances[(nr, nc)] = distances[(r, c)] + 1
        q.append((nr, nc))
  return distances


def rgb_distances(screen):
  targets = {'R': 'G', 'G':'B', 'B':'R'}
  rows, cols = len(screen), len(screen[0])
  res = [[0] * cols for _ in range(rows)]
  for color, targ in targets.items():
    sources = get_sources(screen, targ) #were searching from target -> source
    dist = bfs(screen, sources)

    for i in range(len(screen)):
      for j in range(len(screen[0])):
        if screen[i][j] == color:
          res[i][j] = dist[i,j]
  
  return res

