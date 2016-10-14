
N, K = map(int, raw_input().split())
edge = [[None]*(N+1) for i in xrange(N+1)]

for i in xrange(N):
    edge[i][i] = 0

for _ in xrange(K):
    path = map(int, raw_input().split())
    edge[path[0]][path[1]] = path[2]

for x in xrange(1, N+1):
    for y in xrange(1, N+1):
        if edge[y][x] is None:
          continue
        for z in xrange(1, N+1):
            if edge[x][z] is None:
                continue

            if edge[y][z] is None:
                edge[y][z] = edge[y][x] + edge[x][z]

            elif edge[y][z] > edge[y][x] + edge[x][z]:
                edge[y][z] = edge[y][x] + edge[x][z]

Q = int(raw_input())
for _ in xrange(Q):
    x, y = map(int, raw_input().split())
    ans = edge[x][y]
    if ans is None: ans = -1

    print ans
