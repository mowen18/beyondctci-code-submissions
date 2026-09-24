# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def account_sharing(connections):
    seen = set()
    for ip, name in connections:
      if name in seen:
        return ip
      seen.add(name)
    return ""
