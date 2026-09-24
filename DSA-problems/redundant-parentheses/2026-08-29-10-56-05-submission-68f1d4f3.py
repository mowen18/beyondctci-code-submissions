# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def redundant_parentheses(expression):
  stack = []
  for i in expression:
    if i in '(+-/*':
      stack.append(i)
    elif i == ')':
      if check_redundancy(stack):
        return True
  return False


def check_redundancy(stack):
  is_redundant = True
  while stack[-1] != '(':
    if stack[-1] in '+-/*':
      is_redundant = False
    stack.pop()
  stack.pop()
  return is_redundant

