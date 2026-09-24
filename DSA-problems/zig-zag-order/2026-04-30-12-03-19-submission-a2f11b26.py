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
  if not root:
    return []
  q = deque([root])
  res = []
  depth = 0
  while q:
    level_vals = []
    level_size = len(q)
    for _ in range(level_size):
      node = q.popleft()
      level_vals.append(node.val)

      if node.left:
        q.append(node.left)
      if node.right:
        q.append(node.right)
    if depth % 2 == 1:
      level_vals.reverse()
    res.extend(level_vals)
    depth += 1
  return res

        
      
      
      
      
    

