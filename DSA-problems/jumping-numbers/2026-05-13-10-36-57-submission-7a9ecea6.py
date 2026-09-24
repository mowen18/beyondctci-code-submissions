# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def jumping_numbers(n):
  res = []
  def visit(num):
    if num >= n:
      return
    res.append(num)
    last_digit = num % 10
    if last_digit > 0:
      visit(num * 10 + (last_digit - 1))
    if last_digit < 9:
      visit(num * 10 + (last_digit + 1))
  for i in range(1,10):
    visit(i)
  return sorted(res)
    
