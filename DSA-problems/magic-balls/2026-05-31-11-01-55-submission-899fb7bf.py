# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def magic_balls(r, g, b):
  counts = []
  colors = []
  for count, color in [(r, 'R'), (g, 'G'), (b, 'B')]:
    if count > 0:
      counts.append(count)
      colors.append(color)
    
  
  if len(colors) == 1:
    return colors[0]
  if len(colors) == 3:
    return 'RGB'
  
  missing_color = 'RGB'.replace(colors[0], '').replace(colors[1], '')

  if counts[0] == 1 and counts[1] == 1:
    return missing_color
  if counts[0] > 1 and counts[1] > 1:
    return 'RGB'
  if counts[0] > counts[1]:
    return missing_color + colors[1]
  return missing_color + colors[0]
  
