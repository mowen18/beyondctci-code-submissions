# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
# Available at runtime:
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def most_prolific_level(root):
  levelc = {}
  if not root: return -1
  def visit(node, level):
    if not node:
      return
    
    levelc[level] = levelc.get(level, 0) + 1
    
    visit(node.left, level + 1)
    visit(node.right, level + 1)
  
  visit(root, 0)
  maxprol = 0
  res = 0

  for level in levelc:
    nextlvl = levelc.get(level + 1, 0)
    if nextlvl / levelc[level] > maxprol:
      maxprol = nextlvl / levelc[level]
      res = level
  return res









