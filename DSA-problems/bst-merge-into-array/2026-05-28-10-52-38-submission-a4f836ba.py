# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
# Available at runtime:
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def merge_into_array(root1, root2):
  arr1 = []
  arr2 = []
  def dfs_inorder(node, arr):
    if not node:
      return
    dfs_inorder(node.left, arr)
    arr.append(node.val)
    dfs_inorder(node.right, arr)
  
  dfs_inorder(root1, arr1)
  dfs_inorder(root2, arr2)

  i = j = 0
  res = []
  while i < len(arr1) and j < len(arr2):
    if arr1[i] <= arr2[j]:
      res.append(arr1[i])
      i += 1
    else:
      res.append(arr2[j])
      j += 1
  res.extend(arr1[i:])
  res.extend(arr2[j:])
  return res



