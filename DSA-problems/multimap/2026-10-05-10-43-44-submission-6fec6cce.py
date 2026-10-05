# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
class HashMap:
  def __init__(self, h):
    self.h = h
    self.capacity = 10
    self._size = 0
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


class Multimap:
  def __init__(self, h):
    self.mmap = HashMap(h)
    self._size = 0

  def size(self):
    return self._size

  def contains(self, key):
    return self.mmap.contains(key)

  def get(self, key):
    values = self.mmap.get(key)
    if values is None:
      return []
    return values


  def add(self, key, value):
    values = self.get(key)
    values.append(value)
    self.mmap.add(key, values)
    self._size += 1

  def remove(self, key):
    if self.contains(key):
      self._size -= len(self.get(key))
      self.mmap.remove(key)

