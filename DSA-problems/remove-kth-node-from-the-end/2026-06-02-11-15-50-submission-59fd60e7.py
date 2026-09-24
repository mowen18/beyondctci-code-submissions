# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
# Available at runtime:
#
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#


def remove_kth_node(head, k):
  dummy = ListNode(0)
  dummy.next = head
  slow = dummy
  fast = dummy

  for _ in range(k):
    fast = fast.next
  
  while fast and fast.next:
    fast = fast.next
    slow = slow.next
  
  slow.next = slow.next.next
  return dummy.next

