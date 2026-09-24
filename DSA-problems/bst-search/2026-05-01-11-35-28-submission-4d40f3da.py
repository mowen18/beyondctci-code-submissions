# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
# Available at runtime:
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def contains_target(root, target):
    if target == root:
        return True
    node = root
    while node:
      if node.val == target:
        return True
      elif target > node.val:
        node = node.right
      elif target < node.val:
        node = node.left
    return False
      

