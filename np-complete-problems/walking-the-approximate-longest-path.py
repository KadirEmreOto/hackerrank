from collections import defaultdict
from random import choice, randint
from sys import setrecursionlimit; setrecursionlimit(10 ** 6 + 5)
#from resource import *; setrlimit(RLIMIT_STACK, (RLIM_INFINITY, RLIM_INFINITY))

def DFS(node):
    used[node] = True
    ans.append(node)

    u = [it for it in tree[node] if not used[it]]
    if not u: return
    DFS(choice(u))

n, m = map(int, raw_input().split())
tree = defaultdict(list)

for i in xrange(m):
    x, y = map(int, raw_input().split())

    tree[x].append(y)
    tree[y].append(x)


maxl = 0
res = 0

for i in xrange(350):
    ans = []
    used = [0] * (n+1)
    DFS(randint(1, n))
    if len(ans) > maxl:
        maxl = len(ans)
        res = ans

print maxl
for i in res: print i,


