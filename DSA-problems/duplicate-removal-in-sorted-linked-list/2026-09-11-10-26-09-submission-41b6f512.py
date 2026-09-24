# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
# Available at runtime:
#
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#

class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next
def remove_duplicates(head):
  
  curnode = head
  while curnode and curnode.next:
    if curnode.val == curnode.next.val:
      curnode.next = curnode.next.next
    else:
      curnode = curnode.next
  
  return head

