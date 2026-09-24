# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
# Available at runtime:
#
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#


def compare_lists(headA, headB):
  nodeA = headA
  nodeB = headB
  while nodeA and nodeB:
    if nodeA.val != nodeB.val:
      return False
    nodeA = nodeA.next
    nodeB = nodeB.next
  if nodeA != nodeB: return False
  return True
  

