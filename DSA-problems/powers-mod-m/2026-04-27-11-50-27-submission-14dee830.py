# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def power(a, p, m):
    if p == 0:
        return 1
    if p % 2 == 0:
        half = power(a, p // 2, m)
        return (half * half) % m
    return (a * power(a, p-1, m)) % m
