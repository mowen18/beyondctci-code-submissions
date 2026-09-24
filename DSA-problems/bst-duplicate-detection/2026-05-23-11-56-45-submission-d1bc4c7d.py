# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import math
# Available at runtime:
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def has_duplicate(root):
  prev = -math.inf
  res = False
  def dfs(node):
    nonlocal prev, res
    if not node:
      return
    
    dfs(node.left)
    if node.val == prev:
      res = True
    prev = node.val
    dfs(node.right)
  
  dfs(root)
  return res




      
      


