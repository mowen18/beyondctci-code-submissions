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
    q.append((root, 0))
    curr_depth = 0
    cur_level = []
    res = []
    while q:
      node, depth = q.popleft()
      if not node:
        continue
      if depth > curr_depth:
        if curr_depth % 2 == 0:
          res += cur_level
        else:
          res += cur_level[::-1]
        cur_level = []
        curr_depth = depth
      cur_level.append(node.val)
      q.append((node.left, depth + 1))
      q.append((node.right, depth + 1))
    if cur_level:
      if curr_depth % 2 == 0:
        res += cur_level
      else:
        res += cur_level[::-1]
    return res

      
