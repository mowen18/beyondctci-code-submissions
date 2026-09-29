# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def self_doubling_sequence(n):
  
  def copy_num(n):
    k = 0
    while 2**k <= n:
      k += 1
    
    return k
  
  def f(k, i):
    if k == 1:
      return 1
    first_half = i <= 2 ** (k-2)

    if first_half:
      return f(k - 1, i)
    return f(k, i - 2**(k-2)) + 1
  if n == 0:
    return 0
  k = copy_num(n)
  i = n - 2 ** (k - 1) + 1
  return f(k, i)
