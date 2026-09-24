# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
# Available at runtime:
#
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def reverse_list(head):
  prev = None
  cur = head
  while cur:
    nxt = cur.next
    cur.next = prev
    prev = cur
    cur = nxt
  return prev
def reverse_k_group(head, k):
  dummy = Node(0)
  dummy.next = head
  group_prev = dummy
  while True:
    kth = group_prev
    for _ in range(k):
      kth = kth.next
      if not kth:
        return dummy.next
    group_next = kth.next

    kth.next = None
    group_head = group_prev.next
    reverse_head = reverse_list(group_head)
    group_prev.next = reverse_head
    group_head.next = group_next
    group_prev = group_head


