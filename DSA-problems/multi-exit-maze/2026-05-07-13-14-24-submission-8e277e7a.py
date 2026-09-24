# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
from collections import deque
def exit_distances(maze):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    r, c = len(maze), len(maze[0])
    distances = [[-1] * c for _ in range(r)]
    queue = deque()
    for row in range(r):
      for col in range(c):
        if maze[row][col] == 'O':
          distances[row][col] = 0
          queue.append((row,col))
    while queue:
      noder, nodec = queue.popleft()
      for dir_r, dir_c in directions:
        newr, newc = noder + dir_r, nodec + dir_c
        if 0 <= newr < r and 0 <= newc < c and maze[newr][newc] != 'X' and distances[newr][newc] == -1:
          distances[newr][newc] = distances[noder][nodec] + 1
          queue.append((newr, newc))
        
    return distances


    

