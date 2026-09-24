# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import heapq
def sum_of_powers(primes, k):
  nums = [(i, i) for i in primes]
  res = 0
  m = 10 ** 9 + 7
  heapq.heapify(nums)
  for _ in range(k):
    num, base = heapq.heappop(nums)
    res = (res + num) % m
    heapq.heappush(nums, (num * base, base))
  return res

  
