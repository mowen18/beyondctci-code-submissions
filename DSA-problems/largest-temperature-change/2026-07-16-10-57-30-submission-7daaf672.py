# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def largest_temperature_change(arr, k):
  maxdif = 0
  for i in range(len(arr)-k + 1):
    maxwin = max(arr[i:i+k])
    minwin = min(arr[i:i+k])
    maxdif = max(maxdif, maxwin-minwin)
  return maxdif


