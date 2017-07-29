import sys , resource
#sys.setrecursionlimit(10**5 + 5)
#resource.setrlimit(resource.RLIMIT_STACK, (65532000, 65532000))

class DetectCycle(object):
    def __init__(self, tree, N):
        self.tree = tree

        self.white = range(1, N)
        self.black = [0] * (N+1)
        self.gray  = [0] * (N+1)

    def Run(self):
        node = N
        if self.DFS(node):
            return True
        return False

    def DFS(self, node):
        self.gray[node] = 1

        for it in self.tree[node]:
            if it not in self.tree:
                continue
            if self.black[it]: continue
            if self.gray[it] : return True
            if self.DFS(it): return True

        self.gray[node] = 0
        self.black[node] = 1
        return False

def Fix(node):
    if vis[node]:
        if not dn[node]:
            return 0
        else:
            return 1

    vis[node] = 1
    if 1 in tree[node]:
        dn[node] = 0
        return 0

    check = 1
    for it in tree[node]:
        if dn[it] != -1:
            check *= dn[it]

        else:
            check *= Fix(it)

    dn[node] = check
    return check

def Find(node):

    count = 0
    for it in tree[node]:
        if it not in tree: continue

        if res[it] != -1: count += res[it] * fact[node][it]
        else: count += Find(it) * fact[node][it]

    res[node] = count
    return count

N, M = map(int, raw_input().split())

tree = {}
fact = {}

for _ in xrange(M):
    A, B = map(int, raw_input().split())
    if A not in tree: tree[A] = []
    if B not in tree: tree[B] = []
    if B not in fact: fact[B] = {}

    if A in tree[B]: 
        fact[B][A] += 1

    else:
        fact[B][A] = 1 
        tree[B].append(A)

dn = [-1] * (N + 1)
vis = [0] * (N + 1)
res = [-1] * (N + 1)
res[1] = 1

Fix(N)
for node in xrange(2, N+1):
    if dn[node]:
        try:
            del tree[node] 
        except:
            pass

detect = DetectCycle(tree, N)
if detect.Run(): print 'INFINITE PATHS'

else: print Find(N) % 10**9


