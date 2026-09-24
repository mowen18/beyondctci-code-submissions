# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import heapq
class TopSongs:
  def __init__(self, k):
    self.k = k
    self.mx_heap = []
    self.song_plays = {}

  def register_plays(self, title, plays):
    if title in self.song_plays:
      self.song_plays[title] += plays
    else:
      self.song_plays[title] = plays
    heapq.heappush(self.mx_heap, (-self.song_plays[title], title))



  def top_k(self):
    if self.k == 0: return []
    res = []
    while len(res) < self.k and self.mx_heap:
      plays, title = heapq.heappop(self.mx_heap)
      if -plays == self.song_plays[title]:
        res.append(title)
    for title in res:
      heapq.heappush(self.mx_heap, (-self.song_plays[title], title))
    return res
