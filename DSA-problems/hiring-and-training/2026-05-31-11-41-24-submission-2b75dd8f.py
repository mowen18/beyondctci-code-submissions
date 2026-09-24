# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import math
def hiring_and_training(n):
  def is_divisor(t, n):
    if n % t == 0:
      return True
  
  memo = {}
  def visit(recruiters, untrained):
    if recruiters == n:
      return 0
    if recruiters + untrained > n:
      return math.inf
    
    if (recruiters, untrained) in memo:
      return memo[(recruiters, untrained)]
    
    best = math.inf
    if untrained + recruiters < n:
      best = 1 + visit(recruiters, untrained + recruiters)
    if untrained > 0 and is_divisor(recruiters + untrained, n):
      best = min(best, 1 + visit(recruiters + untrained, 0))
    
    memo[(recruiters, untrained)] = best
    return best
  return visit(1,0)





