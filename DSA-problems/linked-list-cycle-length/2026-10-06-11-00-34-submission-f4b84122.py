# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
# Available at runtime:
#
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
class Node:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def find_start_node(n):
  seen = set()
  node = n
  cnt = 0
  while node:
    mem_ad = id(node)
    if mem_ad in seen:
      return node
    seen.add(mem_ad)
    node = node.next
  return None
def cycle_length(head):
  seen = set()
  startnode = find_start_node(head)
  if startnode is None: return 0
  node = startnode
  mem_ad = id(node)
  seen.add(mem_ad)
  cnt = 1
  while True:
    node = node.next
    mem_ad = id(node)
    if mem_ad in seen:
      break
    seen.add(mem_ad)
    cnt += 1
  return cnt


  

