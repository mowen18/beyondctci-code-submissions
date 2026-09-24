# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
class Node:
  def __init__(self, val = None, next = None):
    self.val = val
    self.next = next
class LinkedListStack:
  def __init__(self):
    self._size = 0
    self.head = None

  def push(self, val):
    newnode = Node(val)
    newnode.next = self.head
    self.head = newnode
    self._size += 1

      
  def pop(self):
    if not self.head: return None
    val = self.head.val
    self.head = self.head.next
    self._size -= 1
    return val
  def peek(self):
    if not self.head: return None
    return self.head.val

  def size(self):
    return self._size

  def empty(self):
    return self._size == 0
