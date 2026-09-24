# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
class Node:
    def __init__(self, val):
        self.prev = None
        self.next = None
        self.val = val


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def size(self):
        return self._size

    def push_front(self, val):
        newnode = Node(val)
        self._size += 1
        if not self.head:
          self.head = newnode
          self.tail = newnode
        else:
          newnode.next = self.head
          self.head.prev = newnode
          self.head = newnode

    def pop_front(self):
        if not self.head:
          return None
        front = self.head.val
        self.head = self.head.next
        if self.head:
          self.prev = None
        else:
          self.tail = None
        self._size -= 1
        return front

    def push_back(self, val):
        back = Node(val)
        if not self.tail:
          self.tail = back
          self.head = back
        else:
          back.prev = self.tail
          self.tail.next = back
          self.tail = back
        self._size += 1


    def pop_back(self):
        if not self.tail:
          return None
        back = self.tail.val
        self.tail = self.tail.prev
        if self.tail:
          self.tail.next = None
        else:
          self.head = None
        self._size -= 1
        return back
      

    def contains(self, val):
        curnode = self.head
        while curnode:
          if curnode.val == val:
            return curnode
          curnode = curnode.next
        return None
