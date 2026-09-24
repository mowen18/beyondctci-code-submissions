# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import heapq
def k_most_played(songs, k):
    min_heap = []
    for song in songs:
        heapq.heappush(min_heap, (song[1], song[0]))
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return [song[1] for song in min_heap]
