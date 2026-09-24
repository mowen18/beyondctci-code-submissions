# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def current_url_with_forward(actions):
    stack = []
    forward_stack = []
    for action in actions:
      val = action[1]
      if action[0] == 'go':
        stack.append(action[1])
      elif action[0] == 'back':
        while len(stack) > 1 and val > 0:
          forward_stack.append(stack.pop())
          val -= 1
      else:
        while len(forward_stack) > 1 and val > 0:
          stack.append(forward_stack.pop())
          val -= 1
    return stack[-1]
