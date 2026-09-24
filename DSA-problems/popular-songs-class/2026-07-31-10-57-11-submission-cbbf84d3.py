# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import heapq
class PopularSongs:
  def __init__(self):
    self.song_plays = {}
    self.upper_minheap = []
    self.lower_mxheap = [] 

  def register_plays(self, title, plays):
    self.song_plays[title] = plays
    if not self.upper_minheap or plays >= self.upper_minheap[0][0]:
      heapq.heappush(self.upper_minheap, (plays, title))
    else:
      heapq.heappush_max(self.lower_mxheap, (plays, title))
    
    if len(self.upper_minheap) > len(self.lower_mxheap) + 1:
      heapq.heappush_max(self.lower_mxheap, heapq.heappop(self.upper_minheap))
    if len(self.lower_mxheap) > len(self.upper_minheap):
      heapq.heappush(self.upper_minheap, heapq.heappop_max(self.lower_mxheap))

  def is_popular(self, title):
    if title not in self.song_plays: return False
    if len(self.lower_mxheap) == len(self.upper_minheap):
      med = (self.lower_mxheap[0][0] + self.upper_minheap[0][0]) / 2
    elif len(self.upper_minheap) > len(self.lower_mxheap):
      med = self.upper_minheap[0][0]
    if self.song_plays[title] > med:
      return True
    return False


