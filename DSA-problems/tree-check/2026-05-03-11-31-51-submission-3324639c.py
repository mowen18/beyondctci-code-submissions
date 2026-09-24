# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def is_tree(graph):
    preds = {0: None}
    has_cycle = False

    def visit(node):
      nonlocal has_cycle

      for nbr in graph[node]:
        if nbr not in preds:
          preds[nbr] = node
          visit(nbr)
        elif nbr != preds[node]:
          has_cycle = True
    visit(0)
    return not has_cycle and len(preds) == len(graph)

