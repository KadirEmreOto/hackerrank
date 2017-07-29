from sys import setrecursionlimit; setrecursionlimit(10 ** 6 + 5)
from resource import *; setrlimit(RLIMIT_STACK, (RLIM_INFINITY, RLIM_INFINITY))

from collections import defaultdict

def DFS(node):
    if used[node]: return
    used[node] = 1

    for it in tree[node]:
        DFS(it)

q = int(raw_input().strip())
for _ in xrange(q):
    n, m, lc, pc = map(int, raw_input().strip().split())

    if lc <= pc:
        print n * lc
        for i in xrange(m): raw_input()
        continue

    sep = 0
    used = [0] * (n+1)
    tree = defaultdict(set)

    for i in xrange(1, n+1): tree[i]

    for i in xrange(m):
        u, v = map(int, raw_input().strip().split())
        tree[u].add(v)
        tree[v].add(u)

    for node in tree:
        if not used[node]:
            DFS(node)
            sep += 1

    print (n  - sep) * pc + lc * sep


