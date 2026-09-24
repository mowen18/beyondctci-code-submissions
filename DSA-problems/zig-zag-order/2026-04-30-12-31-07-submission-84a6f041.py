# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.

from collections import deque
# Available at runtime:
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def zig_zag_order(root):
  q = deque()
  res = []
  q.append((root, 0))
  curr_depth = 0
  curr_level = []
  while q:
    node, depth = q.popleft()
    if not node:
      continue
    if depth > curr_depth:
      if curr_depth % 2 == 0:
        res += curr_level
      else:
        res += curr_level[::-1]
      curr_level = []
      curr_depth = depth
    curr_level.append(node.val)
    q.append((node.left, depth + 1))
    q.append((node.right, depth + 1))
  if curr_level:
    if curr_depth % 2 == 0:
      res += curr_level
    else:
      res += curr_level[::-1]
  return res


      
      
      
      
