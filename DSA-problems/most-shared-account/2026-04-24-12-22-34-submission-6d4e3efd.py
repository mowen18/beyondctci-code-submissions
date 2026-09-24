# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def most_shared_account(connections):
    accts = {}
    for ip, name in connections:
      if not name in accts:
        accts[name] = 1
      else:
        accts[name] += 1
    most_shared = None
    for user, cnt in accts.items():
      if not most_shared or cnt > accts[most_shared]:
        most_shared = user
    return most_shared

    
        
      

