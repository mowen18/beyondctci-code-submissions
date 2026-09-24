# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
# Available at runtime:
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def aligned_chain(root):
  longest = 0
  def dfs(node, depth):
    nonlocal longest
    if not node:
      return 0
    
    left_chain = dfs(node.left, depth + 1)
    right_chain = dfs(node.right, depth + 1)
    curchain = 0
    if node.val == depth:
      curchain = 1 + max(left_chain, right_chain)

      longest = max(longest, curchain)
    return curchain
  dfs(root, 0)
  return longest
