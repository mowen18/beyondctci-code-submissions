# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def unique_movie_titles(titles):
  tit = set()
  for title in titles:
    curtitle = title.split(":")
    tit.add(curtitle[0].lower())
  return list(tit)
