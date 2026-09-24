# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
# Available at runtime:
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def aligned_chain(root):
  max_chain = 0

  def chain(node, depth):
    nonlocal max_chain
    if not node:
      return 0
    
    left_chain = chain(node.left, depth + 1)
    right_chain = chain(node.right, depth + 1)
    currchain = 0
    if node.val == depth:
      currchain = 1 + max(left_chain, right_chain)

      max_chain = max(max_chain, currchain)

    return currchain
  chain(root, 0)
  return max_chain


