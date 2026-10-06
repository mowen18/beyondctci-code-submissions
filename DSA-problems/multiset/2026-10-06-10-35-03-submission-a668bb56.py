# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
class HashMap:
  def __init__(self, h):
    self.h = h
    self._size = 0
    self.capacity = 10
    self.buckets = [[] for _ in range(self.capacity)]
  def size(self):
    return self._size

  def contains(self, k):
    hash = self.h(k, self.capacity)
    for key, _ in self.buckets[hash]:
      if key == k:
        return True
    return False

  def get(self, k):
    hash = self.h(k, self.capacity)
    for key, val in self.buckets[hash]:
      if key == k:
        return val
    return None

  def add(self, k, v):
    hash = self.h(k, self.capacity)
    for i, (key, _) in enumerate(self.buckets[hash]):
      if key == k:
        self.buckets[hash][i] = (k, v)
        return
    self.buckets[hash].append((k, v))
    self._size += 1
    load_factor = self._size / self.capacity
    if load_factor > 1:
      self.resize(self.capacity * 2)

  def remove(self, k):
    hash = self.h(k, self.capacity)
    for i, (key, _) in enumerate(self.buckets[hash]):
      if key == k:
        self.buckets[hash].pop(i)
        self._size -= 1
        load_factor = self._size / self.capacity
        if load_factor < 0.25 and self.capacity > 10:
          self.resize(self.capacity // 2)

  def resize(self, new_capacity):
    new_buckets = [[] for _ in range(new_capacity)]
    for bucket in self.buckets:
      for k, v in bucket:
        hash = self.h(k, new_capacity)
        new_buckets[hash].append((k, v))
    self.buckets = new_buckets
    self.capacity = new_capacity

class Multiset:
  def __init__(self, h):
    self.hmap = HashMap(h)
    self._size = 0

  def size(self):
    return self._size

  def contains(self, x):
    return self.hmap.contains(x)

  def add(self, x):
    count = self.hmap.get(x)
    if count is None:
      self.hmap.add(x, 1)
    else:
      self.hmap.add(x, count + 1)
    self._size += 1

  def remove(self, x):
    count = self.hmap.get(x)
    if count is None:
      return
    if count == 1:
      self.hmap.remove(x)
    else:
      self.hmap.add(x, count - 1)
    self._size -= 1
