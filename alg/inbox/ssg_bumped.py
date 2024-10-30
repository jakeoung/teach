# input: n, m, s, t, k
# input: m lines of u, v, w

from heapq import heappush, heappop
from collections import defaultdict

# input n, m, f, s, t
n, m, f, s, t = map(int, input().split())

# input m lines of u, v, w
graph = defaultdict(list)
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

# input f lines
flights = []
for _ in range(f):
    u, v = map(int, input().split())
    flights.append((u, v))
    # there exists flight from u to v

# construct state space graph where node is (u, used_flight)
# used_flight is integer variable which is 0 or 1
# if used_flight is True, it means that the flight is used

# construct state space graph
# key: (u, used_flight), value: adjacency list from u
ssg = defaultdict(list)

# add an edge to ssg
for u in range(n):
    for v, w in graph[u]:
        ssg[(u, 0)].append(((v, 0), w))
        ssg[(u, 1)].append(((v, 1), w))

# if there exists a flight from u to v
for (u, v) in flights:
    ssg[(u, 0)].append(((v, 1), 0))

# apply dijkstra to ssg
dist = defaultdict(lambda: float('inf'))
dist[(s, 0)] = 0
pq = [(0, (s, 0))]
S = []
while pq:
    d, (u, used_flight) = heappop(pq)
    S.append((u, used_flight))

    for (v, next_used_flight), w in ssg[(u, used_flight)]: # if there exists an edge from u to v
        if (v, next_used_flight) in S:
            continue

        if dist[(v, next_used_flight)] > dist[(u, used_flight)] + w:
            dist[(v, next_used_flight)] = dist[(u, used_flight)] + w
            heappush(pq, (dist[(v, next_used_flight)], (v, next_used_flight)))

print(min(dist[(t, 0)], dist[(t, 1)]))

"""
sample input
8 11 1 0 5
0 1 10
0 2 10
1 2 10
2 6 40
6 7 10
5 6 10
3 5 15
3 6 40
3 4 20
1 4 20
1 3 20
4 7
"""