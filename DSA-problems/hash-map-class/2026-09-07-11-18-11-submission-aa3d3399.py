# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
class HashMap:
  def __init__(self, h):
    self.h = h
    self.capacity = 10
    self._size = 0
    self.buckets = [[] for _ in range(self.capacity)]

  def size(self):
    return self._size

  def contains(self, key):
    hash_ = self.h(key, self.capacity)
    for k, val in self.buckets[hash_]:
      if key == k:
        return True
    return False 


  def get(self, key):
    hash_ = self.h(key, self.capacity)
    for k, val in self.buckets[hash_]:
      if key == k:
        return val
    return

    

  def add(self, key, value):
    hash_ = self.h(key, self.capacity)
    if self.contains(key):
      for i, (k, val) in enumerate(self.buckets[hash_]):
        if key == k:
          self.buckets[hash_].pop(i)
          self.buckets[hash_].append((key, value))
    else:
      self.buckets[hash_].append((key, value))
      self._size += 1
    if self._size / self.capacity > 1:
      self.resize(self.capacity * 2)



  def remove(self, key):
    hash_ = self.h(key, self.capacity)
    for i, (k, val) in enumerate(self.buckets[hash_]):
      if key == k:
        self.buckets[hash_].pop(i)
        self._size -= 1
    lf = self._size / self.capacity
    if lf < 0.25 and self.capacity > 10:
      self.resize(self.capacity // 2)
  def resize(self, new_capacity):
    new_buckets = [[] for _ in range(new_capacity)]
    self.capacity = new_capacity
    for bucket in self.buckets:
      for (key, val) in bucket:
        hash_ = self.h(key, new_capacity)
        new_buckets[hash_].append((key, val))
    self.buckets = new_buckets

