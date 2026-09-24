# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import math
def list_of_divisors(n):
  num = math.floor(math.sqrt(n))
  res = []
  big = []
  for i in range(1, num + 1):
    if n % i == 0:
      res.append(i)
      big.append(n / i)
  
  big.reverse()
  res.extend(big)
  return res


