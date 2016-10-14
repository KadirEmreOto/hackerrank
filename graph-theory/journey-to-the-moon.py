import sys, resource
sys.setrecursionlimit(10**5 + 5)
resource.setrlimit(resource.RLIMIT_STACK, (65532000, 65532000))

def DFS(start, pre=-1):
    count = 0

    for it in tree[start]:
        if it != pre and not c[it]:
            c[it] = 1
            count += DFS(it, start)

    return count + 1

N, L = map(int, raw_input().split())

c = [0]*N
tree = {}
for _ in xrange(L):
    a, b = map(int, raw_input().split())

    if a not in tree: tree[a] = []
    if b not in tree: tree[b] = []

    tree[a].append(b)
    tree[b].append(a)

dn = []
i = 0
while i < N:
    if not c[i]:
        c[i] = 1
        if i not in tree:
            dn.append(1)
            continue

        dn.append(DFS(i))
    i += 1


ans = 0
for i in dn:
    N -= i
    ans += i * N
print ans

