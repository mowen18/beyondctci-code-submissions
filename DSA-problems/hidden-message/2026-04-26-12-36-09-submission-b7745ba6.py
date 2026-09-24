# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
# Available at runtime:
#
# class Node:
#   def __init__(self, text, left=None, right=None):
#     self.text = text
#     self.left = left
#     self.right = right

def hidden_message(root):
  message = []
  
  def visit(node):
    if not node:
      return
    
    elif node.text[0] == 'b':
      message.append(node.text[1])
      visit(node.left)
      visit(node.right)
    elif node.text[0] == 'a':
      visit(node.left)
      visit(node.right)
      message.append(node.text[1])
    else:
      visit(node.left)
      message.append(node.text[1])
      visit(node.right)
  visit(root)
  return "".join(message)
    

