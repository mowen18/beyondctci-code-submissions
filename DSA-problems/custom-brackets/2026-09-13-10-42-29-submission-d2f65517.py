# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def custom_brackets(s, brackets):
  openclose = {}
  closed = set()
  for pair in brackets:
    openclose[pair[0]] = pair[1]
    closed.add(pair[1])
  
  stack = []
  for c in s:
    if c in openclose:
      stack.append(openclose[c])
    elif c in closed:
      if not stack or stack[-1] != c:
        return False
      stack.pop()
  
  return len(stack) == 0
