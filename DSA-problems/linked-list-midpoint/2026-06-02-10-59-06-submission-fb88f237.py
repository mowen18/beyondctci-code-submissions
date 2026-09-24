# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
# Available at runtime:
#
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#


def linked_list_midpoint(head):
  slow, fast = head, head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
  
  return slow.val
