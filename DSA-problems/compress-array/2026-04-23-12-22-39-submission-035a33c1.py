# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def compress_array(arr):
    stack = []
    for num in arr:
      while stack and stack[-1] == num:
        num += stack.pop()
      stack.append(num)
    return stack
