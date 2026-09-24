# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import heapq
def make_playlist_heap(songs):
  
  artist_songs = {}
  for song, artist in songs:
    if artist not in artist_songs:
      artist_songs[artist] = []
    artist_songs[artist].append(song)
  
  mx_heap = []
  for artistname, songlist in artist_songs.items():
    heapq.heappush_max(mx_heap, (len(songlist), artistname, songlist))
  
  res = []
  last_artist = None
  while mx_heap:
    _, artistname1, songlist1 = heapq.heappop_max(mx_heap)
    if artistname1 != last_artist:
      res.append(songlist1.pop())
      if len(songlist1) > 0:
        heapq.heappush(mx_heap, (len(songlist1), artistname1, songlist1))
      last_artist = artistname1
    else:
      if not mx_heap: 
        return []
      _, artistname2, songlist2 = heapq.heappop_max(mx_heap)
      res.append(songlist2.pop())
      last_artist = artistname2
      if len(songlist2) > 0:
        heapq.heappush_max(mx_heap, (len(songlist2), artistname2, songlist2))
      
      heapq.heappush_max(mx_heap, (len(songlist1), artistname1, songlist1))
  return res


