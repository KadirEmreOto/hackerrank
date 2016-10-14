import sys
import heapq

def Dijkstra(node):
    path = [-1] * (N+1)
    path[node] = 0

    queue = []
    visited = [0] * (N+1)

    while node != -1:
        visited[node] = 1

        for child in tree[node]:
            cost = path[node]

            if path[child[0]] == -1:
                path[child[0]] = max(child[1], cost)
                heapq.heappush(queue, (path[child[0]], child[0]))

            elif not visited[child[0]]:
                path[child[0]] = min(path[child[0]], max(cost , child[1]))
                heapq.heappush(queue, (path[child[0]], child[0]))

        node = -1
        best = sys.maxint

        while queue:
            node = heapq.heappop(queue)[1]

            if not visited[node]:
                break
    
    return path[-1]
    

N, E = map(int, raw_input().split())
tree = {}

for _ in xrange(E):
    x, y, c = map(int, raw_input().split())

    if x not in tree: tree[x] = []
    if y not in tree: tree[y] = []

    tree[x].append((y, c))
    tree[y].append((x, c))

ans = Dijkstra(1)
if ans == -1:
    ans = 'NO PATH EXISTS'

print ans

