# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import heapq
def presidential_election(candidates, votes):
  total_sum = sum(votes)

  min_heap = []
  for i in range(len(votes)):
    min_heap.append((votes[i], candidates[i]))
    if votes[i] > total_sum // 2:
      return candidates[i]
  votes_needed = total_sum // 2
  heapq.heapify(min_heap)
  sum_votes = 0
  while min_heap and sum_votes <= votes_needed:
    smallest1 = heapq.heappop(min_heap)
    smallest2 = heapq.heappop(min_heap)
    if smallest1[0] == smallest2[0]:
      candidate = min(smallest1[1], smallest2[1])
    else:
      candidate = smallest2[1]
    sum_votes += smallest1[0] + smallest2[0]
    
    while min_heap and smallest2[0] == min_heap[0][0]:
      next_smallest = heapq.heappop(min_heap)
      sum_votes += next_smallest[0]
      candidate = min(candidate, next_smallest[1])
    if sum_votes > votes_needed:
      return candidate
    heapq.heappush(min_heap, (sum_votes, candidate))
  return candidate






