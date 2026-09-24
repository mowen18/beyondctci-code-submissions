# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
from collections import deque
class MaxQueue:
  def __init__(self):
    self.queue = deque()
    self.maxq = deque()

  def peek(self):
    return self.queue[0]

  def size(self):
    return len(self.queue)

  def max(self):
    return self.maxq[0]

  def pop(self):
    val = self.queue[0]
    if val == self.maxq[0]:
        self.maxq.popleft()
    return self.queue.popleft()
    

  def push(self, val):
    self.queue.append(val)
    while self.maxq and self.maxq[-1] < val:
        self.maxq.pop()
    self.maxq.append(val)

