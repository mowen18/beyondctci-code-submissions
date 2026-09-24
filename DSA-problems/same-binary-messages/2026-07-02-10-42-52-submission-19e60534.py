# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def same_messages(arr):
  stack1 = []
  stack2 = []
  for num in arr:
    if num == 0 or num == 1:
      stack1.append(num)
    elif num == 2 and len(stack1) > 0:
      stack1.pop()
    elif num == 10:
      stack2.append(0)
    elif num == 11:
      stack2.append(1)
    elif num == 12 and len(stack2) > 0:
      stack2.pop()
  return stack1 == stack2

