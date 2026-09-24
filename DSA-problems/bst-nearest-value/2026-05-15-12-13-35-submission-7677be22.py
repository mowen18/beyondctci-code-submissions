# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
# Available at runtime:
import math
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_closest(root, target):
  next_above, next_below = math.inf, -math.inf
  curnode = root
  while curnode:
    if curnode.val == target:
      return curnode.val
    elif curnode.val > target:
      next_above = curnode.val
      curnode = curnode.left
    else:
      next_below = curnode.val
      curnode = curnode.right
  if next_above - target < target - next_below:
    return next_above
  return next_below
    
    
