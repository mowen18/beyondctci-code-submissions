# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
# Available at runtime:
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def aligned_path(root):
    res = 0

    def visit(node, depth):
        nonlocal res
        if not node:
            return 0
        
        left_chain = visit(node.left, depth + 1)
        right_chain = visit(node.right, depth + 1)
        current_chain = 0
        if node.val == depth:
            current_chain = max(left_chain, right_chain) + 1

            res = max(res, left_chain + right_chain + 1)
        return current_chain

    visit(root, 0)
    return res


