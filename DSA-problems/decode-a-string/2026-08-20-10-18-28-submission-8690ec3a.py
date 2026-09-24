# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def decode_string(s):
  count_stack = []
  str_stack = []
  curr_str = []
  k = 0
  for char in s:
    if char.isdigit():
      k = k * 10 + int(char)
    elif char == "{":
      count_stack.append(k)
      str_stack.append(curr_str)
      curr_str = []
      k = 0
    elif char == "}":
      multiplier = count_stack.pop()
      prevstring = str_stack.pop()
      curr_str = prevstring + curr_str * multiplier
    else:
      curr_str.append(char)
  return "".join(curr_str)



