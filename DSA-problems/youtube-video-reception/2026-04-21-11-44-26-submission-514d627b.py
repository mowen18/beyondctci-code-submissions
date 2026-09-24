# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def youtube_video_reception(likes, dislikes, periods):
   pos_neg = []
   for i in range(len(likes)):
      if likes[i] > dislikes[i]:
          pos_neg.append(1)
      else:
        pos_neg.append(0)
   prefix_sum = []
   prefix_sum.append(pos_neg[0])
   for i in range(1, len(pos_neg)):
      prefix_sum.append(prefix_sum[i-1] + pos_neg[i])
   res = []
   for i, j in periods:
      if i == 0:
          res.append(prefix_sum[j])
      else:
          res.append(prefix_sum[j] - prefix_sum[i - 1])
   return res
    
