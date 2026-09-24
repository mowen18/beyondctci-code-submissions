# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
# Available at runtime:
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def tree_diameter(root):
    heights = {}
    def height(node):
        if not node:
            return 0
    
        max_height = 1 + max(height(node.left), height(node.right))
        heights[node] = max_height
        return max_height
    height(root)
    
    def diameter(node):
        if not node:
            return 0
        
        left_path = heights[node.left] if node.left else 0
        right_path = heights[node.right] if node.right else 0
        both = left_path + right_path

        left_diam = diameter(node.left)
        right_diam = diameter(node.right)
        return max(both, left_diam, right_diam)
    return diameter(root)




