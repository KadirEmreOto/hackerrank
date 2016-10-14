import sys
sys.setrecursionlimit(10**5 + 5)
INF = sys.maxint

def DFS(node, pre):
    global SUM, MAX
    dist1 = -INF
    dist2 = -INF

    for n, c in tree[node]:
        if n != pre:
            dist1 = max(dist1, DFS(n, node) + c)
            if dist1 > dist2:
                dist1, dist2 = dist2, dist1

            dp[node] += dp[n]
            if 0 < dp[n] < K:
                SUM += c

    if dist1 > 0: MAX = max(MAX, dist1 + dist2)
    if dist2 > 0 and dv[node]: MAX = max(MAX, dist2)
    if dv[node]: dist2 = max(0, dist2)

    return dist2


N, K = map(int, raw_input().split())
delv = map(int, raw_input().split())

tree = {}
dp = [0] * (N+5)
dv = [0] * (N+5)

for i in delv: dp[i] = dv[i] = 1

for i in xrange(N-1):
    x, y, c = map(int, raw_input().split())

    if x not in tree: tree[x] = []
    if y not in tree: tree[y] = []

    tree[x].append([y, c])
    tree[y].append([x, c])

SUM = 0
MAX = 0
DFS(1,1)
print SUM * 2 - MAX

