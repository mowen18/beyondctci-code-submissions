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
def node_at_index(head, index):
  if index < 0:
    return None
  
  cur = head
  i = 0
  while cur:
    if i == index:
      return cur
    cur = cur.next
    i += 1
  
  if i == index:
    return cur
  return None

def reverse_list(head):
  prev = None
  cur = head
  while cur:
    nxt = cur.next
    cur.next = prev
    prev = cur
    cur = nxt
  return prev
def reverse_section(head, left, right):

  dummy = Node(0)
  dummy.next = head
  
  if left == 0:
    prev = dummy
  else:
    prev = node_at_index(head, left - 1)
  
  if not prev or not prev.next:
    return head
  nxt = node_at_index(head, right + 1)
  section_head = prev.next
  prev.next = None
  section_tail = section_head
  while section_tail.next != nxt:
    section_tail = section_tail.next
  section_tail.next = None

  old_section_head = section_head
  new_section_head = reverse_list(section_head)

  prev.next = new_section_head
  old_section_head.next = nxt

  return dummy.next









