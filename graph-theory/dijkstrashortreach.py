import sys
import heapq

def Dijkstra(node):
    queue = [(0, node)]

    while queue:
        node = heapq.heappop(queue)[1]
        cost = path[node]
        visited[node] = 1

        for i, r in tree[node]:
            if path[i] == -1:
                path[i] = cost + r
            elif cost + r < path[i]:
                path[i] = cost + r
                visited[i] = 0

            if not visited[i]:
                heapq.heappush(queue, (path[i], i))
                visited[i] = 1

if __name__ == '__main__':
    T = int(raw_input())

    for t0 in xrange(T):
        N, M = map(int, raw_input().split())
        tree = {}
        path = [-1] * (N+1)
        visited = [0] * (N+1)

        for m0 in xrange(M):
            x, y, r = map(int, raw_input().split())

            if x not in tree: tree[x] = []
            tree[x].append((y, r))

            if y not in tree: tree[y] = []
            tree[y].append((x, r))

        S = int(raw_input())
        path[S] = 0

        Dijkstra(S)

        for i in path[1:]:
            if i != 0:
                print i,
        print
