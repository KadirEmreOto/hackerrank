import sys

def DFS(node, pre=-1):
    if tree[node][-1] == '*': dp[node].append(sys.maxint)
    else: dp[node].append(0)
    dp[node].append(0)

    for it in tree[node]:
        if it == '*': continue

        if it[0] != pre:
            DFS(it[0], node)
            dp[node][1] += min(dp[it[0]][0], dp[it[0]][1] + it[1])
            dp[node][1] = min(dp[node][1], dp[node][0] + dp[it[0]][1])
            if (tree[node] != '*'):
                dp[node][0] += min(dp[it[0]][0], dp[it[0]][1] + it[1])


N, K = map(int, raw_input().split())
tree = {}

for _ in xrange(N-1):
    x, y, z = map(int, raw_input().split())

    if x not in tree: tree[x] = []
    if y not in tree: tree[y] = []

    tree[x].append((y, z))
    tree[y].append((x, z))

for _ in xrange(K):
    m = int(raw_input())
    tree[m].append('*')

dp = [[] for i in xrange(N)]
DFS(0)

print min(dp[0][0], dp[0][1])
