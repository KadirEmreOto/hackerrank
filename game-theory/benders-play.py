from collections import defaultdict

def grundy(n):
    if n not in gnum: return 0
    if gnum[n] != None: return gnum[n]

    s = set([])
    for it in tree[n]:
        s.add(grundy(it))

    for i in xrange(10**5):
        if i not in s:
            gnum[n] = i
            return i

N, M = map(int, raw_input().split())

gnum = {}
tree = defaultdict(list)
for i in xrange(M):
    x, y = map(int, raw_input().split())
    tree[x].append(y)

    gnum[x] = None
    gnum[y] = None


Q = int(raw_input())
for i in xrange(Q):
    num = int(raw_input())
    pos = map(int, raw_input().split())

    ans = 0
    for it in pos:
        ans ^= grundy(it)
    if ans > 0: print 'Bumi'
    else: print 'Iroh'

