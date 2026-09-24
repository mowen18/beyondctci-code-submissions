# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def most_frequent_octet(ips):
    octscnt = {}
    for octet in ips:
      firsto = octet.split('.')[0]
      if not firsto in octscnt:
        octscnt[firsto] = 1
      else:
        octscnt[firsto] += 1
    most_freq = None
    for i, j in octscnt.items():
      if not most_freq or octscnt[most_freq] < j:
        most_freq = i
    return most_freq
