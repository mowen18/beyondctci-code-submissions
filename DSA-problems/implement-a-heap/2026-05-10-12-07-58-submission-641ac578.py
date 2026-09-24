# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
class Heap:
    def __init__(self, higher_priority = lambda x, y : x < y, heap = None):
        self.higher_priority = higher_priority
        if heap:
          self.heap = heap
          self.heapify()
        else:
          self.heap = []

    def size(self):
        return len(self.heap)

    def top(self):
        if len(self.heap) > 0:
          return self.heap[0]
        return None

    def push(self, elem):
        self.heap.append(elem)
        self._bubble_up(len(self.heap)-1)
        

    def pop(self):
        if len(self.heap) == 0: return None
        top = self.heap[0]
        if len(self.heap) == 1:
          self.heap = []
          return top
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._bubble_down(0)
        return top
          

    def heapify(self):
        for idx in range(len(self.heap) // 2, -1, -1):
          self._bubble_down(idx)

    def _parent(self, idx):
        if idx == 0:
          return -1
        return (idx - 1) // 2

    def _left_child(self, idx):
        return idx * 2 + 1

    def _right_child(self, idx):
        return idx * 2 + 2

    def _bubble_up(self, idx):
        if idx == 0:
          return
        p_idx = self._parent(idx)
        if self.higher_priority(self.heap[idx], self.heap[p_idx]):
          self.heap[p_idx], self.heap[idx] = self.heap[idx], self.heap[p_idx]
          self._bubble_up(p_idx)

    def _bubble_down(self, idx):
        left_i = self._left_child(idx)
        right_i = self._right_child(idx)
        if left_i >= len(self.heap): return
        child_i = left_i
        if right_i < len(self.heap) and self.higher_priority(self.heap[right_i], self.heap[left_i]):
          child_i = right_i
        if self.higher_priority(self.heap[child_i], self.heap[idx]):
          self.heap[idx], self.heap[child_i] = self.heap[child_i], self.heap[idx]
          self._bubble_down(child_i)
         
