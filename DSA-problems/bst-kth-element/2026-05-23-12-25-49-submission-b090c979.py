# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
# Available at runtime:
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def kth_element(root, k):
  steps = 0
  res = None
  def dfs(node):
    nonlocal steps, res
    if not node:
      return
    dfs(node.left)
    if steps == k:
      res = node.val
    steps += 1
    dfs(node.right)
  dfs(root)
  return res

