# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def image_filter(img):
  if len(img) == 0: return img
  R, C = len(img),len(img[0])
  res = [[0] * C for _ in range(R)]
  dirs = [(1,0), (0,1), (-1,0), (0,-1), (0,0), (1, 1), (-1, -1), (1, -1),  (-1, 1)]
  def is_valid(row, col):
    return 0 <= row < R and 0 <= col < C
  
  for row in range(R):
    for col in range(C):
      count = 0
      s_avg = 0
      for mr, mc in dirs:
        new_r = mr + row
        new_c = mc + col
        if is_valid(new_r, new_c):
          s_avg += img[new_r][new_c]
          count += 1
      res[row][col] = s_avg // count
  return res


  

  


