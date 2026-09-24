# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def longest_stable_period(temperatures, t):
    cnt = 0
    maxdays = 0
    curmax= 1
    for i in range(len(temperatures) - 1):
        cnt = 1
        for j in range(i + 1, len(temperatures)):
            if abs(temperatures[j] - temperatures[j - 1]) <= t:
                cnt += 1
                curmax = max(curmax, cnt)
            else:
                cnt = 1
        maxdays = max(maxdays, curmax)
    return maxdays
