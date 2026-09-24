# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import math
def center_assignment(points, center1, center2):
  def dist(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
  n = len(points)
  assignment = [0] * len(points)
  res = 0
  for i, p in enumerate(points):
    if dist(p, center1) <= dist(p, center2):
      res += dist(p, center1)
      assignment[i] = 1
    else:
      res += dist(p, center2)
      assignment[i] = 2
  
  c1_cnt = assignment.count(1)

  switch_cost = []
  for i, p in enumerate(points):
    if assignment[i] == 1 and c1_cnt > n // 2:
      switch_cost.append(dist(p, center2) - dist(p, center1))
    if assignment[i] == 2 and c1_cnt < n // 2:
      switch_cost.append(dist(p, center1) - dist(p, center2))
  
  switch_cost.sort()
  for cost in switch_cost[:abs(c1_cnt - n // 2)]:
    res += cost
  return res

  

