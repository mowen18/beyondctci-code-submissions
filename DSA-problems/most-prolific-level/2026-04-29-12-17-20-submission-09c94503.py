# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
from collections import deque, defaultdict
# Available at runtime:
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def most_prolific_level(root):
    q = deque()
    q.append((root, 0))
    lvlc = defaultdict(int)
    while q:
      node, depth = q.popleft()
      if not node:
        continue
      lvlc[depth] += 1
      q.append((node.left, depth + 1))
      q.append((node.right, depth + 1))
    most_p = -1
    res = -1
    if len(lvlc) == 1:
      return 0
    for i in range(len(lvlc) - 1):
      current_lvl = lvlc[i]
      next_lvl = lvlc.get(i + 1, 0)
      if next_lvl / current_lvl > most_p:
        most_p = next_lvl / current_lvl
        res = i
    return res
    
      




