# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def king_kong_vs_godzilla_in_the_fog(street, k):
  def kong(street):
    stack = []
    nge = [-1] * len(street)

    for i in range(len(street) - 1, -1, -1):
      while stack and street[stack[-1]] <= street[i]:
        stack.pop()
      if stack:
        nge[i] = stack[-1]
      stack.append(i)

    res1 = []
    for i in range(len(street)):
      if nge[i] != -1 and nge[i] <= i + k:
        res1.append(True)
      else:
        res1.append(False)
    return res1

  def zilla(street):
    street2 = [-i for i in street]
    street2.reverse()
    res2 = kong(street2)
    res2.reverse()
    return res2

  final1 = kong(street)
  final2 = zilla(street)

  return [a and b for a, b in zip(final1, final2)]