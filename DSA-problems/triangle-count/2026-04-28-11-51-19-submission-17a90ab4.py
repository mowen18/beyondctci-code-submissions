# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
# Available at runtime:
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def triangle_count(root):
    res = 0

    def visit(node):
        nonlocal res
        if not node:
            return 0, 0
        left, _ = visit(node.left)
        _, right = visit(node.right)

        res += min(left, right)
        return (left + 1, right + 1)
    visit(root)
    return res

    
    



