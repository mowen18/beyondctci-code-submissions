# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
class HashMap:
  def __init__(self, h):
    self.h = h
    self.capacity = 10
    self.buckets = [[] for _ in range(self.capacity)]
    self._size = 0

  def size(self):
    return self._size

  def contains(self, key):
    hsh = self.h(key, self.capacity)
    for ky, val in self.buckets[hsh]:
      if ky == key:
        return True
    return False

  def get(self, key):
    h = self.h(key, self.capacity)
    for ky, val in self.buckets[h]:
      if ky == key:
        return val
    return None

  def add(self, key, value):
    hsh = self.h(key, self.capacity)
    for i, (ky, _) in enumerate(self.buckets[hsh]):
      if ky == key:
        self.buckets[hsh][i] = (key, value)
        return
    self.buckets[hsh].append((key, value))
    self._size += 1
    load_factor = self._size / self.capacity
    if load_factor > 1:
      self.resize(self.capacity * 2)
  
  def resize(self, new_capacity):
    news_buckets = [[] for _ in range(new_capacity)]
    for bucket in self.buckets:
      for k, v in bucket:
        hsh = self.h(k, new_capacity)
        news_buckets[hsh].append((k,v))
    self.buckets = news_buckets
    self.capacity = new_capacity


  def remove(self, key):
    hsh = self.h(key, self.capacity)
    for i, (k, _) in enumerate(self.buckets[hsh]):
      if k == key:
        self.buckets[hsh].pop(i)
        self._size -= 1
        load_factor = self._size / self.capacity
        if load_factor < 0.25 and self.capacity > 10:
          self.resize(self.capacity // 2)

  def keys(self):
    result = []
    for bucket in self.buckets:
      for k, _ in bucket:
        result.append(k)
    return result

  def values(self):
    result = []
    for bucket in self.buckets:
      for _, v in bucket:
        result.append(v)
    return result
