# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
import math

def seg_dist(min1, max1, min2, max2):
    return max(0, max(min1, min2) - min(max1, max2))

def distance(furn1, furn2):
    x_min1, y_min1, x_max1, y_max1 = furn1
    x_min2, y_min2, x_max2, y_max2 = furn2
    x_gap = seg_dist(x_min1, x_max1, x_min2, x_max2)
    y_gap = seg_dist(y_min1, y_max1, y_min2, y_max2)
    if x_gap == 0:
        return y_gap
    elif y_gap == 0:
        return x_gap
    else:
        return math.sqrt(x_gap**2 + y_gap**2)

def can_reach(furniture, d):
    V = len(furniture)
    graph = [[] for _ in range(V)]
    
    for i in range(V):
        for j in range(i + 1, V):
            if distance(furniture[i], furniture[j]) <= d:
                graph[i].append(j)
                graph[j].append(i)

    visited = set()
    visited.add(0)
    def visit(node):

        for nbr in graph[node]:
            if not nbr in visited:
                visited.add(nbr)
                visit(nbr)
    visit(0)
    return V - 1 in visited
    



