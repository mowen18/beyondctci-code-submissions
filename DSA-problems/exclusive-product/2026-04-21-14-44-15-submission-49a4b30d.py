# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def exclusive_product(arr):
    m = 10**9 + 7
    n = len(arr)
    prefix = []
    prefix.append(arr[0])
    for i in range(1, len(arr)):
      prefix.append(prefix[i-1] * arr[i] % m)
    post = [1] * n
    post[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
      post[i] = post[i+1] * arr[i] % m
    
    res = [1] * n
    res[n-1] = prefix[n-2]
    res[0] = post[1]
    for i in range(1, len(arr) - 1):
      res[i] = prefix[i-1] * post[i+1] % m
    return res
    


