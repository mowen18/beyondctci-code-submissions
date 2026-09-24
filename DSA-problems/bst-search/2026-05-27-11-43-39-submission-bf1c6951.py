# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
# Available at runtime:
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def contains_target(root, target):
  contains = False
  def visit(node):
    nonlocal contains
    if not node:
      return
    elif node.val < target:
      visit(node.right)
    elif node.val > target:
      visit(node.left)
    else:
      if node.val == target:
        contains = True
  visit(root)
  return contains
