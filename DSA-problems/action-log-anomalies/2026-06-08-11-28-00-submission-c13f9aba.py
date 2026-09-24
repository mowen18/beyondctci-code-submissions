# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def find_anomalies(log):
  anomalies = set()
  working_on = {}
  actiontick = {}
  seen = set()
  opened = {}
  for agent, action, ticket in log:
    if agent in working_on and working_on[agent] != ticket:
      anomalies.add(working_on[agent])
    
    if ticket in anomalies:
      continue
    
    if action == 'open' and ticket in seen:
      anomalies.add(ticket)
      continue
    elif action == 'open':
      seen.add(ticket)
      working_on[agent] = ticket
      opened[ticket] = agent
    else:
      if ticket in opened and opened[ticket] == agent:
        del working_on[agent]
        del opened[ticket]
      else:
        anomalies.add(ticket)
        continue
  print(anomalies)
  anomalies.update(opened.keys())
  return list(anomalies)
      

    


