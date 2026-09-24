# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
from collections import deque
# Available at runtime:
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def left_view(root):
    if not root:
      return []
    q = deque()
    q.append((root, 0))
    res = [root.val]
    current_depth = 0
    while q:
      node, depth = q.popleft()
      if not node:
        continue
      if current_depth + 1 == depth:
        res.append(node.val)
        current_depth += 1
      q.append((node.left, depth +1 ))
      q.append((node.right, depth + 1))
    return res

