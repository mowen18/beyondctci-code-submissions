# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
# Available at runtime:
#
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
class Node:
  def __init__(self, val=0, next = None):
    self.val = val
    self.next = next

def merge(head1, head2):
  dummy = Node(0)
  cur = dummy
  node1 = head1
  node2 = head2 
  while node1 and node2:
    cur.next = node1
    cur = cur.next
    node1 = node1.next
    cur.next = node2
    node2 = node2.next
    cur = cur.next
  
  if node1:
    cur.next = node1
  if node2:
    cur.next = node2
  
  return dummy.next






  
  
