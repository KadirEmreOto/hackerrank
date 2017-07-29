from collections import defaultdict
from sys import setrecursionlimit; setrecursionlimit(10 ** 6 + 5)
from resource import *; setrlimit(RLIMIT_STACK, (RLIM_INFINITY, RLIM_INFINITY))

def Solve(node, col, pcol, pre):
    if dp[node][col][pcol] != -1:
        return dp[node][col][pcol]

    if len(graph[node]) == 1 and node != 1:
        if col == pcol:
            dp[node][col][pcol] = 1
            return 1
        dp[node][col][pcol] = 0
        return 0

    dp[node][col][pcol] = 1
    for it in graph[node]:
        if it != pre:
            dp[node][col][pcol] = (dp[node][col][pcol]*((Solve(it, 0, col, node)+Solve(it, 1, col, node))%M)) % M

    if col != pcol:
        d = 1

        for it in graph[node]:
            if it != pre:
                d = (d*dp[it][col^1][col]) % M
        dp[node][col][pcol] = (dp[node][col][pcol] - d) % M

    return dp[node][col][pcol]

M = 10**9 + 7
N = int(raw_input())
if N == 1:
    print 2

else:
    graph = defaultdict(list)

    for i in xrange(N-1):
        u, v = map(int, raw_input().split())

        graph[u].append(v)
        graph[v].append(u)

    dp = [[[-1]*2 for i in xrange(2)] for i in xrange((10**5)+10)]
    print (2 * Solve(1, 0, 1, 0)) % M


