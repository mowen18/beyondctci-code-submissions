# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def validate_html(html):

  def get_tag_details(index):
    i = index + 1
    open_tag = True
    if i < len(html) and html[i] == '/':
      open_tag = False
      i += 1
    
    j = i
    while j < len(html) and html[j] != '>':
      j += 1
    tag = html[i:j]
    return [open_tag, tag]
  
  stack = []
  for i in range(len(html)):
    if html[i] == '<':
      is_open, tag = get_tag_details(i)
    
      if is_open:
        stack.append(tag)
      elif not stack or stack[-1] != tag:
        return False
      else:
        stack.pop()
  
  return not stack
  


