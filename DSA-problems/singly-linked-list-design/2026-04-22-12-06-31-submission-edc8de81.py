# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def size(self):
        return self._size

    def push_front(self, val):
        newnode = Node(val)
        newnode.next = self.head
        self.head = newnode
        self._size +=1
    def pop_front(self):
        if not self.head:
          return None
        val = self.head.val
        self.head = self.head.next
        self._size -= 1
        return val

    def push_back(self, val):
        newnode = Node(val)
        self._size +=1
        if not self.head:
          self.head = newnode
          return
        cur = self.head
        while cur.next:
          cur = cur.next
        cur.next = newnode

    def pop_back(self):
        if not self.head:
          return None
        self._size -= 1
        if not self.head.next:
          val = self.head.val
          self.head = None
          return val
        cur = self.head
        while cur.next and cur.next.next:
          cur = cur.next
        val = cur.next
        cur.next = None
        return val

    def contains(self, val):
        cur = self.head
        while cur:
          if cur.val == val:
            return cur
          cur = cur.next
        return None
