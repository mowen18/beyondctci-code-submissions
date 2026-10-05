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
    hsh = self.h(x, self.capacity)
    for elem in self.buckets[hsh]:
      if elem == x:
        return True
    return False

  def add(self, x):
    hsh = self.h(x, self.capacity)
    for elem in self.buckets[hsh]:
      if elem == x: return
    self.buckets[hsh].append(x)
    load = self._size / self.capacity
    if load > 1:
      self.resize(self.capacity * 2)
    self._size += 1
  
  def resize(self, new_cap):
    newbuckets = [[] for _ in range(new_cap)]
    for bucket in self.buckets:
      for elem in bucket:
        hsh = self.h(elem, new_cap)
        newbuckets[hsh].append(elem)
    self.buckets = newbuckets
    self.capacity = new_cap


  def remove(self, x):
    hsh = self.h(x, self.capacity)
    for i, elem in enumerate(self.buckets[hsh]):
      if elem == x:
        self.buckets[hsh].pop(i)
        self._size -= 1
        load = self._size / self.capacity
        if load < 0.25 and self._size > 10:
          self.resize(self.capacity // 2)

  def elements(self):
    res = []
    for bucket in self.buckets:
      for elem in bucket:
        res.append(elem)
    return res

  def union(self, s):
    newhset = HashSet(self.h)
    for elem in self.elements():
      newhset.add(elem)
    for elem2 in s.elements():
      newhset.add(elem2)
    return newhset

  def intersection(self, s):
    newhset = HashSet(self.h)
    for elem in self.elements():
      if elem in s.elements():
        newhset.add(elem)
    return newhset
    
