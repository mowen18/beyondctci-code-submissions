# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import math
# Available at runtime:
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def is_bst(root):
  prev_val = -math.inf
  res = True

  def visit(node):
      nonlocal prev_val, res
      if not node or not res:
        return
      visit(node.left)
      if node.val < prev_val:
        res = False
      else:
        prev_val = node.val

      visit(node.right)
  visit(root)
  return res


      


