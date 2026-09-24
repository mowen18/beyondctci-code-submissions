# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def next_greater_element(arr):

  nge = [-1 for _ in range(len(arr))]
  stack = []

  for i in range(len(arr)-1, -1, -1):

    while stack and arr[stack[-1]] <= arr[i]:
      stack.pop()
    if stack:
      nge[i] = stack[-1]
    
    stack.append(i)
  return nge

