# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None
    self.prev = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self._size = 0

  def size(self):
    return self._size

  def push_front(self, val):
    new = Node(val)
    if not self.head:
      self.head = new
      self.tail = new
    else:
      new.next = self.head
      self.head.prev = new
      self.head = new
    self._size += 1


  def pop_front(self):
    if not self.head:
      return None
    val = self.head.val
    self.head = self.head.next
    if self.head:
      self.head.prev = None
    else:
      self.tail = None
    self._size -= 1
    return val

  def push_back(self, val):
    new = Node(val)
    if not self.tail:
      self.head = self.tail = new
    else:
      new.prev = self.tail
      self.tail.next = new
      self.tail = new
    self._size += 1


  def pop_back(self):
    if not self.tail:
      return None
    val = self.tail.val
    self.tail = self.tail.prev
    if self.tail:
      self.tail.next = None
    else:
      self.head = self.tail = None
    self._size -= 1
    return val


  def contains(self, val):
    cur = self.head
    while cur:
      if cur.val == val:
        return cur
      cur = cur.next
    return None

