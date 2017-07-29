from fractions import Fraction
from collections import defaultdict

def walk(node, pre=None):
    global cur
    for it in tree[node]:
        if it != pre:
            if it in par[node]:
                cur += 1
            walk(it, node)

def DFS(node, pre=None):
    global w, cur
    if cur >= k: w += 1

    for it in tree[node]:
        if it != pre:
            r = (node in par[it]) - (it in par[node])

            cur += r
            DFS(it, node)
            cur -= r

for _ in xrange(int(raw_input())):
    n = int(raw_input())
    tree = defaultdict(list)

    for i in xrange(n-1):
        u, v = map(int, raw_input().split())
        tree[u].append(v)
        tree[v].append(u)

    g, k = map(int, raw_input().split())
    par = defaultdict(set)

    for i in xrange(g):
        u, v = map(int, raw_input().split())
        par[u].add(v)

    cur, w = 0, 0
    walk(1)
    DFS(1)

    if w == 0: print '0/1'
    elif Fraction(w, n) == 1: print '1/1'
    else: print Fraction(w, n)


