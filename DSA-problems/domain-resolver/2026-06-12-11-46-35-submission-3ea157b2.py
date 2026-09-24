# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
class DomainResolver:
  def __init__(self):
    self.iptodomain = {}
    self.domaintosub = {}

  def register_domain(self, ip, domain):
    self.iptodomain[domain] = ip
    self.domaintosub[domain] = []


  def register_subdomain(self, domain, subdomain):
    self.domaintosub[domain].append(subdomain)

  def has_subdomain(self, ip, domain, subdomain):
    if self.iptodomain[domain] != ip:
      return False
    if subdomain not in self.domaintosub[domain]:
      return False
    return True
