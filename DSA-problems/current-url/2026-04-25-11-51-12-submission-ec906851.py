# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def current_url(actions):
    stack = []

    for action in actions:
      backnum = action[1]
      if action[0] == 'go':
        stack.append(action[1])
      else:
        while len(stack) > backnum and backnum > 0:
          stack.pop()
          backnum -= 1
    return stack[-1]

        
