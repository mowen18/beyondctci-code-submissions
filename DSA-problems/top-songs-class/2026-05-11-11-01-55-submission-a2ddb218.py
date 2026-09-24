# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import heapq
class TopSongs:
    def __init__(self, k):
        self.songs = []
        self.k = k

    def register_plays(self, title, plays):
        self.songs.append([title, plays])

    def top_k(self):
        minheap = []
        for song in self.songs:
            heapq.heappush(minheap, (song[1], song[0]))
            if len(minheap) > self.k:
                heapq.heappop(minheap)
        return [song[1] for song in minheap]
            
        
