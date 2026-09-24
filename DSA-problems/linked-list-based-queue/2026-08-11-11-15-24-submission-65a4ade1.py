# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
class Node:
  def __init__(self, val):
    self.next = None
    self.val = val
class LinkedListQueue:
  def __init__(self):
    self.head = None
    self.tail = None
    self._size = 0

  def empty(self):
    return self._size == 0

  def size(self):
    return self._size

  def push(self, val):
    newnode = Node(val)
    if self._size == 0:
      self.head = newnode
      self.tail = newnode
    else:
      lastnode = self.tail
      lastnode.next = newnode
      self.tail = newnode
    self._size += 1

  def pop(self):
    if self._size == 0: 
      return None
    curnode = self.head.val
    self.head = self.head.next
    self._size -= 1
    return curnode

  def peek(self):
    if self._size == 0:
      return None
    curnode = self.head
    return curnode.val
