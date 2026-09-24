# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
class HashSet:
  def __init__(self, h):
    self.h = h
    self.capacity = 10
    self.buckets = [[] for _ in range(self.capacity)]
    self._size = 0

  def size(self):
    return self._size
  def contains(self, x):
    hash_ = self.h(x, self.capacity)
    for elem in self.buckets[hash_]:
      if elem == x:
        return True
    return False

  def add(self, x):
    hash_ = self.h(x, self.capacity)
    self.buckets[hash_].append(x)
    self._size += 1
    if self._size / self.capacity == 1:
      self.resize(self.capacity * 2)
      


  def remove(self, x):
    hash_ = self.h(x, self.capacity)
    for i, elem in enumerate(self.buckets[hash_]):
      if elem == x:
        self.buckets[hash_].pop(i)
        self._size -= 1
    lf = self._size / self.capacity
    if lf < 0.25 and self.capacity > 10:
      self.resize(self.capacity // 2)



  def resize(self, new_capacity):
    new_buckets = [[] for _ in range(new_capacity)]
    self.capacity = new_capacity
    for bucket in self.buckets:
      for elem in bucket:
        hash_ = self.h(elem, new_capacity)
        new_buckets[hash_].append(elem)
    self.buckets = new_buckets
