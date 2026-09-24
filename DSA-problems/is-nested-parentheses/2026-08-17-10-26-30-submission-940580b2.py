# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def is_nested_parentheses(s):
  if len(s) == 0:
    return True
  if s[0] == "(" and s[-1] == ")":
    return is_nested_parentheses(s[1:-1])
  return False
