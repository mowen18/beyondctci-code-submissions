# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
# Available at runtime:
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def left_view(root):
  depths = []
  seen = set()
  def visit(node, depth):
    
    if not node:
      return
    if depth not in seen:
      seen.add(depth)
      depths.append(node.val)
    visit(node.left, depth + 1)
    visit(node.right, depth + 1)
  
  visit(root, 0)
  return depths


