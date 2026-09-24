# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
# Available at runtime:
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
def most_protected_node(root):
    protectionlvl = {}
    nodelevelindex = {}
    nodedepthc = {}
    def bfs(node, depth):
        q = deque()
        q.append((node, depth))

        while q:
            node, depth = q.popleft()
            if not node:
                continue
            if depth not in nodedepthc:
                nodedepthc[depth] = 0
            nodedepthc[depth] += 1
            nodelevelindex[node] = nodedepthc[depth] - 1
            protectionlvl[node] = min(depth, nodelevelindex[node])
            q.append((node.left, depth + 1))
            q.append((node.right, depth + 1))
    bfs(root, 0)
    def dfs(node, depth):
        if not node:
            return -1
        height = 1 + max(dfs(node.left, depth + 1), dfs(node.right, depth + 1))

        protectionlvl[node] = min(protectionlvl[node], height)

        protectionlvl[node] = min(protectionlvl[node], nodedepthc[depth] - nodelevelindex[node] - 1)

        return height
    dfs(root, 0)
    return max(protectionlvl.values())

    







