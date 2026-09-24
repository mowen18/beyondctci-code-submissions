# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import heapq
def top_k_across_genres(genres, k):
  mxheap = []
  for genre_index, song_list in enumerate(genres):
    plays = song_list[0][1]
    heapq.heappush_max(mxheap, (plays, genre_index, 0))
  
  topk = []
  while len(topk) < k and mxheap:
    plays, genre_index, song_index = heapq.heappop_max(mxheap)
    song_name = genres[genre_index][song_index][0]
    topk.append(song_name)

    song_index += 1
    if song_index < len(genres[genre_index]):
      plays = genres[genre_index][song_index][1]
      heapq.heappush_max(mxheap, (plays, genre_index, song_index))
  return topk
  
