# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
# Available at runtime:
#
class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


def convert_to_array(node):
    while node.prev:
        node = node.prev
    arr = []
    while node:
        arr.append(node.val)
        node = node.next
    return arr


