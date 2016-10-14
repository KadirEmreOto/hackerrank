from collections import defaultdict, deque

tree = defaultdict(list)
N, M = map(int, raw_input().split())
N = 1111
for e in xrange(M):
    x, y, c = map(int, raw_input().split())

    tree[x].append([y, c])
    tree[y].append([x, c])

a, b = map(int, raw_input().split())

used = [[False] * N for n in xrange(N)]

queue = deque()
queue.append((a, 0))

while queue:
    ver, res = queue.popleft()

    used[ver][res] = True

    for it in tree[ver]:
        if not used[it[0]][(it[1] | res)]:
            used[it[0]][(it[1] | res)] = True
            queue.append((it[0], it[1] | res))

ans = -1
for i in xrange(N):
    if used[b][i]:
        ans = i
        break
print ans

