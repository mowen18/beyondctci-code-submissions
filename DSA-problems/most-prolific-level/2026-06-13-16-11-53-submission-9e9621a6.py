# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
from collections import deque
# Available at runtime:
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def most_prolific_level(root):
    q = deque()
    q.append((root, 0))
    levelc = {}
    while q:
        node, depth = q.popleft()
        if not node: continue
        if depth not in levelc:
            levelc[depth] = 0
        levelc[depth] += 1

        q.append((node.left, depth + 1))
        q.append((node.right, depth + 1))
    maxprol = -1
    res = -1
    for level in levelc:
        next_levelc = levelc.get(level + 1, 0)
        prol = next_levelc / levelc[level]
        if prol > maxprol:
            maxprol = prol
            res = level
    return res


