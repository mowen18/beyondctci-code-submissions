# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def count_subarrays_with_sum_k(arr, k):

    prefix_sums = [0 for _ in range(len(arr))]
    prefix_sums[0] = arr[0]
    for i in range(1, len(arr)):
        prefix_sums[i] = prefix_sums[i - 1] + arr[i]
    
    sub_sumc = {0: 1}
    count = 0
    for val in prefix_sums:
        if val - k in sub_sumc:
            count += sub_sumc[val - k]
        if val not in sub_sumc:
            sub_sumc[val] = 0
        sub_sumc[val] += 1
    return count



