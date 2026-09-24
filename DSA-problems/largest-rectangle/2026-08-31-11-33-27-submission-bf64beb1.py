# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def largest_rectangle(tiles):
  nsm = next_smallest(tiles)
  psm = prev_smallest(tiles)
  n = len(tiles)
  max_area = 0
  for i in range(n):
    width = nsm[i] - psm[i] - 1
    height = tiles[i]
    area = width * height
    max_area = max(max_area, area)
  return max_area

def prev_smallest(arr):
  n = len(arr)
  stack = []
  pse = [-1] * n
  for i in range(n):
    while stack and arr[stack[-1]] >= arr[i]:
      stack.pop()
  
    if stack:
      pse[i] = stack[-1]
    stack.append(i)
  return pse
def next_smallest(arr):
  n = len(arr)
  stack = []
  nse = [n] * n
  for i in range(n - 1, -1, -1):
    while stack and arr[stack[-1]] >= arr[i]:
      stack.pop()
  
    if stack:
      nse[i] = stack[-1]
    stack.append(i)
  return nse


