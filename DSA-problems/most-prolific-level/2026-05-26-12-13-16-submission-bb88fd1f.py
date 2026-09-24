# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
from collections import deque
# Available at runtime:
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def most_prolific_level(root):
  queue = deque()

  depth_count = {}
  queue.append((root, 0))
  while queue:
    node, depth = queue.popleft()
    if not node:
      continue
    if depth not in depth_count:
      depth_count[depth] = 0
    depth_count[depth] += 1
    queue.append((node.left, depth + 1))
    queue.append((node.right, depth + 1))

  res = -1
  max_lvl = -1
  for level in depth_count:
    next_lvl = depth_count.get(level + 1, 0)
    cnt = next_lvl / depth_count[level]
    if cnt > max_lvl:
      max_lvl = cnt
      res = level
  return res



