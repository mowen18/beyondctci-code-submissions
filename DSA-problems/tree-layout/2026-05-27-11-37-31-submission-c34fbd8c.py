# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
# Available at runtime:
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def tree_layout(root):
  visited = {}
  def visit(node, r, c):
    if not node:
      return
    if (r, c) not in visited:
      visited[(r,c)] = 0
    visited[(r,c)] += 1
    visit(node.left, r + 1, c)
    visit(node.right, r, c + 1)
  visit(root, 0, 0)
  return max(visited.values())

    


