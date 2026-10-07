# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
class Matrix:
  def __init__(self, grid):
    self.matrix = [row.copy() for row in grid]

  def transpose(self):
    matrix = self.matrix
    for r in range(len(matrix)):
      for c in range(r):
        matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
    self.matrix = matrix
  def reflect_horizontally(self):
    for row in self.matrix:
      row.reverse()

  def reflect_vertically(self):
    self.matrix.reverse()

  def rotate_clockwise(self):
    self.transpose()
    self.reflect_horizontally()


  def rotate_counterclockwise(self):
    self.transpose()
    self.reflect_vertically()
