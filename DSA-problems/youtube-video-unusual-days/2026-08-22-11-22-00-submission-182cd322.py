# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def youtube_video_unusual_days(likes, dislikes):
  n = len(likes)
  scores = [likes[i] - dislikes[i] for i in range(n)]
  scores.sort()
  prefix_sums = [0 for _ in range(n)]
  prefix_sums[0] = scores[0]
  for i in range(1, n):
    prefix_sums[i] = prefix_sums[i-1] + scores[i]
  
  max_deviation = 0
  for i in range(n):
    left, right = 0, 0
    if i > 0:
      left = i * scores[i] - prefix_sums[i-1]
    if i < n - 1:
      right = prefix_sums[n-1] - prefix_sums[i] - (n - i - 1) * scores[i]
    max_deviation = max(max_deviation, left + right)
  return max_deviation


