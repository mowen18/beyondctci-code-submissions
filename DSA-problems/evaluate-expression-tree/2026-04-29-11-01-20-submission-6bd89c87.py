# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
# Available at runtime:
#
# class Node:
#   def __init__(self, kind, num, children):
#     self.kind = kind          # One of "sum", "product", "max", "min", or "num".
#     self.num = num            # Only valid when kind is "num".
#     self.children = children  # Only valid when kind is not "num".

def product(lis):
  result = 1
  for i in lis:
    result *= i
  return result

def evaluate(root):
  res = []
  if root.kind == 'num':
    return root.num
  for child in root.children:
    res.append(evaluate(child))
  if root.kind == 'sum':
    return sum(res)
  if root.kind == 'product':
    return product(res)
  if root.kind == 'min':
    return min(res)
  if root.kind == 'max':
    return max(res)
  return res



