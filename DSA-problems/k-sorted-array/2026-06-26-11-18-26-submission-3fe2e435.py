# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import heapq
def k_sorted_array(arr, k):
    heap = []
    for i in range(min(k + 1, len(arr))):
        heapq.heappush(heap, arr[i])
    res = []
    next_to_add = k + 1
    while heap:

        res.append(heapq.heappop(heap))

        if next_to_add < len(arr):
            heapq.heappush(heap, arr[next_to_add])
            next_to_add += 1
    return res


        





    

