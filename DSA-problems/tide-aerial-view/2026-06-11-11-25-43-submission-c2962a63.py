# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def tide_aerial_view(pictures):

  numpic = len(pictures)
  cells = len(pictures[0]) ** 2

  def ones_in_row(row):
    if row[0] == 0:
      return 0
    if row[-1] == 1:
      return len(row)
    
    l, r = 0, len(row) - 1
    while r - l > 1:
      mid = (r + l) // 2
      if row[mid] == 1:
        l = mid
      else:
        r = mid
    return r


  def num_ones(picture):
    ones = 0
    for rows in picture:
      ones += ones_in_row(rows)
    
    return ones
  def balanced(picture):
    numones = num_ones(picture)
    ncells = len(picture[0]) ** 2
    return abs(2 * numones - ncells)
  def is_before(pic):
    celln = len(pic[0]) ** 2
    total_ones = num_ones(pic)
    return total_ones / celln < 0.5
  
  l, r = 0, numpic - 1
  while r - l > 1:
    mid = (l+r) // 2
    if is_before(pictures[mid]):
      l = mid
    else:
      r = mid
  
  candidater = pictures[r]
  candidatel = pictures[l]
  if balanced(candidatel) == balanced(candidater):
    return l
  return r




