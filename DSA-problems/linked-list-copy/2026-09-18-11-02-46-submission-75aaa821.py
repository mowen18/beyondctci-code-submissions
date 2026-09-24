# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
# Available at runtime:
#
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#

class Node:
  def __init__(self, val = 0, next = None):
    self.val = val
    self.next = next
def copy_list_with_dummy(head):
  
  if not head:
    return []
  if not head.next:
    node = Node(head.val)
    return node
  new_head = Node(head.val)
  cur_new = new_head
  cur_old = head.next
  while cur_old:
    cur_new.next = Node(cur_old.val)
    cur_new = cur_new.next
    cur_old = cur_old.next



  return new_head

