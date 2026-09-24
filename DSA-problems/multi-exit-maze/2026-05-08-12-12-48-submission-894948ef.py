# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
from collections import deque
def exit_distances(maze):
    R, C = len(maze), len(maze[0])
    dists = [[-1] * C for _ in range(R)]
    dirs = [(1,0),(-1, 0), (0, 1), (0, -1)]
    queue = deque()
    for r in range(R):
      for c in range(C):
        if maze[r][c] == 'O':
          dists[r][c] = 0
          queue.append((r,c))
    while queue:
      noder, nodec = queue.popleft()
      for x, y in dirs:
        next_r, next_c = noder + x, nodec + y
        if (0 <= next_r < R and 0 <= next_c < C and maze[next_r][next_c] != 'X' and dists[next_r][next_c] == -1):
          dists[next_r][next_c] = dists[noder][nodec] + 1
          queue.append((next_r, next_c))
    return dists






