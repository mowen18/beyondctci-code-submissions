# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import math
def are_circles_nested(circles):

  def contains(c1, c2):
    (x1, y1), r1 = c1[0], c1[1]
    (x2, y2), r2 = c2[0], c2[1]

    distance = math.sqrt((x1 - x2)**2 + (y1-y2)**2)

    return distance + r2 < r1
  
  circles.sort(key = lambda x: x[1], reverse= True)

  for i in range(len(circles) - 1):
    if not contains(circles[i], circles[i + 1]):
      return False
  
  return True


