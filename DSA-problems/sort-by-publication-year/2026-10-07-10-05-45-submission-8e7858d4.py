# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
# Available at runtime:
#
class Book:
    def __init__(self, title, author, page_count, genre, year_published):
        self.title = title
        self.author = author
        self.page_count = page_count
        self.genre = genre
        self.year_published = year_published


def bucket_sort(books):
  if not books: return []
  min_year = min([book.year_published for book in books])
  max_year = max([book.year_published for book in books])
  buckets = [[] for _ in range(max_year - min_year + 1)]
  for book in books:
    buckets[book.year_published - min_year].append(book)
  
  res = []
  for bucket in buckets:
    for book in bucket:
      res.append(book)
  
  return res
  

  

