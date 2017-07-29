#-*- coding: UTF-8 -*-
from heapq import heappop, heappush
from collections import defaultdict

n, m, k = map(int, raw_input().split())

masks = [0] * (n+1)
graph = [[] for i in xrange(n+1)]
dp = [[float('inf')]*((1<<k)+2) for i in xrange(n+1)]

for i in xrange(1, n+1):
    ar = map(int, raw_input().split())
    for t in xrange(1, len(ar)):
        masks[i] |= 1 << ar[t]-1

for i in xrange(m):
    u, v, c = map(int, raw_input().split())
    graph[u].append((v, c))
    graph[v].append((u, c))

queue = [(0, 1, masks[1])]

while queue:
    cost, node, mask = heappop(queue)

    for it in graph[node]:
        if cost + it[1] < dp[it[0]][mask | masks[it[0]]]:
            heappush(queue, (cost+it[1], it[0], mask | masks[it[0]]))
            dp[it[0]][mask | masks[it[0]]] = cost + it[1]

ans = float('inf')
for i in xrange(1 << k):
    if dp[n][i] == float('inf'): continue

    for j in xrange(1 << k):
        if i | j == (1 << k) - 1 and dp[n][j] != float('inf'):
            ans = min(ans, max(dp[n][i], dp[n][j]))
print ans

