# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def multi_account_cheating(users):
    ips = set()
    for i in users:
      if tuple(sorted(i[1])) in ips:
        return True
      else:
        ips.add(tuple(sorted(i[1])))
    return False

