# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def minimum_steps_to_one(n):
  
  memo = {}
  def num_steps(i):
    if i == 1:
      return 0
    if i in memo:
      return memo[i]
    steps = num_steps(i - 1)
    if i % 2 == 0:
      steps = min(steps, num_steps(i // 2))
    if i % 3 == 0:
      steps = min(steps, num_steps(i // 3))
    memo[i] = steps + 1
    return memo[i]
  return num_steps(n)
    
    

