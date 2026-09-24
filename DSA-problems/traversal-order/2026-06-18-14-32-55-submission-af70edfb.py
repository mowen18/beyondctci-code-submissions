# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
# Available at runtime:
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def traversal_order(root, order):
  res = []
  def preorder(node):
    if not node:
      return
    res.append(node.val)
    preorder(node.left)
    preorder(node.right)
  
  def inorder(node):
    if not node:
      return
    inorder(node.left)
    res.append(node.val)
    inorder(node.right)
  def postorder(node):
    if not node:
      return
    postorder(node.left)
    postorder(node.right)
    res.append(node.val)
  
  if order == 1:
    preorder(root)
  elif order == 2:
    inorder(root)
  else:
    postorder(root)
  return res
    
    
