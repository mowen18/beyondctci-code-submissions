# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def compute_inner_parentheses(s):
  
  if s[0] != '(':
    return compute_inner_parentheses(s[1:])
  if s[-1] != ')':
    return compute_inner_parentheses(s[:-1])
  return s
