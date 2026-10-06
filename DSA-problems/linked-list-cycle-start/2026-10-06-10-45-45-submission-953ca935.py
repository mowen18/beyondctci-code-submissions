# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
# Available at runtime:
#
class Node:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def cycle_start(head):
  seen = set()
  node = head
  while node:
    mem_ad = id(node)
    if mem_ad in seen:
      return node
    seen.add(mem_ad)
    node = node.next
  return None
