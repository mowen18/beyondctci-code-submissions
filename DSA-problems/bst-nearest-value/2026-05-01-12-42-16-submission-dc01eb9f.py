# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import math
# Available at runtime:
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def find_closest(root, target):
    curr_node = root
    next_above, next_below = math.inf, -math.inf
    while curr_node:
      if curr_node.val == target:
        return curr_node.val
      elif curr_node.val > target:
        next_above = curr_node.val
        curr_node = curr_node.left
      else:
        next_below = curr_node.val
        curr_node = curr_node.right
    
    if next_above - target < target - next_below:
      return next_above
    return next_below

