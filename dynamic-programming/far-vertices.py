from random import shuffle
from collections import defaultdict

def DFS(node, pre=None, cost=0, main=None):
    if main is None: main = node
    dist[main].add(main)
    for it in tree[node]:
        if it != pre:
            dist[main].add(it)
            if cost < K-1:
                DFS(it, node, cost+1, main)

def Solve():
    stack = range(1, N+1)
    shuffle(stack)

    answer = 0
    visited = [0] * (N+1)

    for node in stack:
        if not visited[node]:
            visited[node] = 1
            for it in xrange(1, N+1):
                if not visited[it] and it not in dist[node]:
                    answer += 1
                    visited[it] = 1

    return answer


N, K = map(int, raw_input().split())
tree = defaultdict(list)
dist = defaultdict(set)

for n in xrange(N-1):
    x, y = map(int, raw_input().split())

    tree[x].append(y)
    tree[y].append(x)

for node in xrange(1, N+1):
    DFS(node)

answer = 124235324
for i in xrange(100):
    answer = min(answer, Solve())
print answer

