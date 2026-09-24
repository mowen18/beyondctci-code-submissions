# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
from collections import deque

class ViewerCounter:
    def __init__(self, window):
        self.window = window
        self.queues = {'subscriber': deque(), 'guest': deque(), 'follower': deque()}

    def join(self, t, v):
        self._remove_old_viewers(t)
        self.queues[v].append(t)

    def get_viewers(self, t, v):
        self._remove_old_viewers(t)
        return len(self.queues[v])

    def _remove_old_viewers(self, t):
        for queue in self.queues.values():
          while queue and queue[0] < t - self.window:
            queue.popleft()
