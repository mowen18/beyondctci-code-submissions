# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def os_paths(path, readlink):
  stack = []
  for part in path.split("/"):
    if part in [".", ""]:
      continue
    elif part == '..':
      if stack:
        stack.pop()
    elif part in readlink:
      if part[0] == "~":
        stack.append('home')
      else:
        for link in readlink[part].split("/"):
          if link == "":
            stack.clear()
          stack.append(link)
    elif part:
      stack.append(part)
  
  return '/' + '/'.join(stack)

      

